--
-- PostgreSQL database dump
--

-- Dumped from database version 10.1
-- Dumped by pg_dump version 10.1

-- Started on 2017-11-19 00:53:53

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SET check_function_bodies = false;
SET client_min_messages = warning;
SET row_security = off;

SET search_path = public, pg_catalog;

--
-- TOC entry 2970 (class 0 OID 16791)
-- Dependencies: 245
-- Data for Name: rttApp_tasks; Type: TABLE DATA; Schema: public; Owner: django-app-client
--

COPY "rttApp_tasks" (id, "timestamp", task_date, original_location, task_description, fix_description, management_comments, date_completed, date_created, date_updated, asset_id, replacement_asset_id, resolved_by_user_id, state_id, submitted_by_user_id, task_category_id) FROM stdin;
1	2017-11-18 13:30:51.143259-08	2017-11-17 13:30:25-08	Office	Computer fails to boot properly, will get past BIOS, and then sits at a blank screen with a blinking cursor.			\N	2017-11-18 13:30:51.155291-08	2017-11-18 13:30:51.155291-08	1	2	\N	1	1	2
\.


--
-- TOC entry 2975 (class 0 OID 0)
-- Dependencies: 244
-- Name: rttApp_tasks_id_seq; Type: SEQUENCE SET; Schema: public; Owner: django-app-client
--

SELECT pg_catalog.setval('"rttApp_tasks_id_seq"', 1, true);


-- Completed on 2017-11-19 00:53:53

--
-- PostgreSQL database dump complete
--

