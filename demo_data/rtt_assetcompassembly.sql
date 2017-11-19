--
-- PostgreSQL database dump
--

-- Dumped from database version 10.1
-- Dumped by pg_dump version 10.1

-- Started on 2017-11-19 00:50:47

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
-- TOC entry 2960 (class 0 OID 16715)
-- Dependencies: 231
-- Data for Name: rttApp_assetcomponentassembly; Type: TABLE DATA; Schema: public; Owner: django-app-client
--

COPY "rttApp_assetcomponentassembly" (id, date_created, date_updated, asset_id, component_id) FROM stdin;
1	2017-11-17 23:21:42.545606-08	2017-11-17 23:21:42.545606-08	1	1
2	2017-11-17 23:21:48.303612-08	2017-11-17 23:21:48.303612-08	2	2
3	2017-11-17 23:21:54.226478-08	2017-11-17 23:21:54.226478-08	4	3
\.


--
-- TOC entry 2965 (class 0 OID 0)
-- Dependencies: 230
-- Name: rttApp_assetcomponentassembly_id_seq; Type: SEQUENCE SET; Schema: public; Owner: django-app-client
--

SELECT pg_catalog.setval('"rttApp_assetcomponentassembly_id_seq"', 3, true);


-- Completed on 2017-11-19 00:50:47

--
-- PostgreSQL database dump complete
--

