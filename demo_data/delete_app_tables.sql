-- 
-- Deletes tables from keysApp and rttApp 
-- 


SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SET check_function_bodies = false;
SET client_min_messages = warning;
SET row_security = off;

SET search_path = public, pg_catalog;

DELETE FROM "keysApp_records";
DELETE FROM "keysApp_loanexceptions";
DELETE FROM "keysApp_loanterms";
DELETE FROM "keysApp_customers"
DELETE FROM "keysApp_affiliations";
DELETE FROM "keysApp_departments";
DELETE FROM "keysApp_keys";
DELETE FROM "keysApp_keytypes";

DELETE FROM "rttApp_tasks";
DELETE FROM "rttApp_assetcomponentassembly";
DELETE FROM "rttApp_states";
DELETE FROM "rttApp_categories";
DELETE FROM "rttApp_components";
DELETE FROM "rttApp_assets";
DELETE FROM "rttApp_makemodel";
DELETE FROM "rttApp_makers";
