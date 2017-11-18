# App-level Schema
import graphene
from graphene_django import DjangoObjectType
from graphql import GraphQLError
import pdb

from rttApp.models import Makers, MakeModel, Assets, Categories, States, Components, AssetComponentAssembly, Tasks
from django.contrib.auth.models import User
from django.db.models import Q

class MakersType(DjangoObjectType):
    """For looking at Makers (manufacturers)"""
    class Meta:
        model = Makers

class MakeModelType(DjangoObjectType):
    class Meta:
        model = MakeModel

class AssetsType(DjangoObjectType):
    class Meta:
        model = Assets

class CategoriesType(DjangoObjectType):
    class Meta:
        model = Categories

class StatesType(DjangoObjectType):
    class Meta:
        model = States

class ComponentsType(DjangoObjectType):
    class Meta:
        model = Components

class AssetComponentAssemblyType(DjangoObjectType):
    class Meta:
        model = AssetComponentAssembly

class TasksType(DjangoObjectType):
    class Meta:
        model = Tasks

class UsersType(DjangoObjectType):
    class Meta:
        model = User

class Query(object):
    # all of a table
    all_makers = graphene.List(MakersType)
    all_models = graphene.List(MakeModelType)
    all_assets = graphene.List(AssetsType)
    all_categories = graphene.List(CategoriesType)
    all_states = graphene.List(StatesType)
    all_components = graphene.List(ComponentsType)
    all_asset_component_assemblies = graphene.List(AssetComponentAssemblyType)
    # all_tasks = graphene.List(TasksType) #deprecated

    # search types
    tasks = graphene.List(TasksType, assetNumber=graphene.Int())
    task = graphene.Field(TasksType, taskID=graphene.ID())

    def resolve_all_makers(self, info):
        return Makers.objects.all()

    def resolve_all_models(self, info):
        return MakeModel.objects.all()

    def resolve_all_assets(self, info):
        return Assets.objects.all()

    def resolve_all_categories(self, info):
        return Categories.objects.all()

    def resolve_all_states(self, info):
        return States.objects.all()

    def resolve_all_components(self, info):
        return Components.objects.all()

    def resolve_all_asset_component_assemblies(self, info):
        return AssetComponentAssembly.objects.all()

    # def resolve_all_tasks(self, info):
    #     return Tasks.objects.all()

    def resolve_tasks(self, info, **kwargs):
        if 'assetNumber' in kwargs:
            filter = (
                Q(asset__number__istartswith=kwargs.get('assetNumber'))
            )
            return Tasks.objects.filter(filter).order_by('-timestamp')
        return Tasks.objects.all().order_by('-timestamp')

    def resolve_task(self, info, taskID):
        if taskID is not None:
            return Tasks.objects.get(pk=taskID)
        return None

class CreateMaker(graphene.Mutation):
    key = graphene.ID()
    maker = graphene.String()
    date_created = graphene.types.datetime.DateTime()

    class Arguments:
        maker = graphene.String(required=True)

    @staticmethod
    def mutate(root, input, context, info):
        new_maker = Makers(maker=input.get('maker'),)
        new_maker.save()
        new_maker.refresh_from_db()

        return CreateMaker(
            key=new_maker.pk,
            maker=new_maker.maker,
            date_created=new_maker.date_created,
        )

class CreateMakeModel(graphene.Mutation):
    key = graphene.ID()
    make = graphene.String()
    model_name = graphene.String()
    description = graphene.String()
    date_created = graphene.types.datetime.DateTime()

    class Arguments:
        make = graphene.ID(required=True)
        model_name = graphene.String(required=True)
        description = graphene.String(required=True)

    @staticmethod
    def mutate(root, info, **args):
        query_make = Makers.objects.filter(pk=input.get('make')).first()
        if not query_make:
            raise GraphQLError("Specified manufacturer does not exist.")
        new_make_model = MakeModel(
            make=query_make,
            model_name=input.get('model_name'),
            description=input.get('description'),
        )
        new_make_model.save()
        new_make_model.refresh_from_db()

        return CreateMakeModel(
            key=new_make_model.pk,
            make=new_make_model.make.maker,
            model_name=new_make_model.model_name,
            description=new_make_model.description,
            date_created=new_make_model.date_created,
        )

class CreateAsset(graphene.Mutation):
    key = graphene.ID()
    model = graphene.String()
    number = graphene.Int()
    serial = graphene.String()
    description = graphene.String()
    mac_address = graphene.String()
    notes = graphene.String()
    date_created = graphene.types.datetime.DateTime()

    class Arguments:
        model = graphene.ID(required=True)
        number = graphene.Int(required=True)
        serial = graphene.String(required=True)
        description = graphene.String()
        mac_address = graphene.String(required=True)
        notes = graphene.String()

    @staticmethod
    def mutate(root, info, **args):
        query_model = MakeModel.objects.filter(pk=input.get('model')).first()
        if not query_model:
            raise GraphQLError("Specified model does not exist.")
        new_asset = Assets(
            model=query_model,
            number=input.get('number'),
            serial=input.get('serial'),
            description=input.get('description'),
            mac_address=input.get('mac_address'),
            notes=input.get('notes'),
        )
        new_asset.save()
        new_asset.refresh_from_db()

        return CreateAsset(
            key=new_asset.pk,
            model=new_asset.model.model_name,
            number=new_asset.number,
            serial=new_asset.serial,
            description=new_asset.description,
            mac_address=new_asset.mac_address,
            notes=new_asset.notes,
            date_created=new_asset.date_created,
        )

class CreateTask(graphene.Mutation):
    key = graphene.ID()
    timestamp = graphene.types.datetime.DateTime()
    asset = graphene.String()
    submitter = graphene.String()
    task_date = graphene.types.datetime.DateTime()
    location = graphene.String()
    category = graphene.String()
    description = graphene.String()
    replacement_asset = graphene.String()
    state = graphene.String()
    date_created = graphene.types.datetime.DateTime()

    class Arguments:
        #expect timestamp to be something like Date("2015-03-25T12:00:00Z")
        timestamp = graphene.types.datetime.DateTime(required=True)
        asset = graphene.ID(required=True)
        submitter = graphene.ID(required=True)
        task_date = graphene.types.datetime.DateTime()
        location = graphene.String(required=True)
        category = graphene.ID(required=True)
        description = graphene.String(required=True)
        replacement_asset = graphene.ID()

    @staticmethod
    def mutate(root, info, **args):
        query_asset = Assets.objects.filter(pk=input.get('asset')).first()
        if not query_asset:
            raise GraphQLError("Specified Asset not found.")
        query_submitter = User.objects.filter(pk=input.get('submitter')).first()
        if not query_submitter:
            raise GraphQLError("Specified User not found.")
        query_category = Categories.objects.filter(pk=input.get('category')).first()
        if not query_category:
            raise GraphQLError("Specified Category not found.")
        #optional values
        query_replacement = input.get('replacement_asset')
        if query_replacement:
            query_replacement = Assets.objects.filter(pk=query_replacement).first()
            pdb.set_trace()
            if not query_replacement:
                raise GraphQLError("Specified replacement asset not found.")
        input_task_date = input.get('task_date')

        # Create a new task with known available values first, then add in optional values.
        new_task = Tasks(
            timestamp=input.get('timestamp'),
            asset=query_asset,
            submitted_by_user=query_submitter,
            original_location=input.get('location'),
            task_category=query_category,
            task_description=input.get('description'),
            state=States.objects.filter(state__iexact='new').get(),
        )
        if query_replacement:
            new_task.replacement_asset=query_replacement
        if input_task_date:
            new_task.task_date=input_task_date
        new_task.save()
        new_task.refresh_from_db()

        return CreateTask(
            key=new_task.pk,
            timestamp=new_task.timestamp,
            asset=new_task.asset,
            submitter=new_task.submitted_by_user,
            task_date=new_task.task_date,
            location=new_task.original_location,
            category=new_task.task_category,
            description=new_task.task_description,
            replacement_asset=new_task.replacement_asset,
            state=new_task.state,
            date_created=new_task.date_created,
        )

class Mutation(object):
    """Register all mutation classes to graphene endpoint"""
    create_maker = CreateMaker.Field()
    create_make_model = CreateMakeModel.Field()
    create_asset = CreateAsset.Field()
    create_task = CreateTask.Field()
