--
-- PostgreSQL database dump
--

-- Dumped from database version 10.1
-- Dumped by pg_dump version 10.1

-- Started on 2017-11-19 00:51:51

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
-- TOC entry 2959 (class 0 OID 16739)
-- Dependencies: 235
-- Data for Name: rttApp_categories; Type: TABLE DATA; Schema: public; Owner: django-app-client
--

COPY "rttApp_categories" (id, category, description, date_created, date_updated) FROM stdin;
1	Standard Reimage	Computer needs to be re-imaged, but no other maintenance issues noted.	2017-11-17 23:18:08.671497-08	2017-11-17 23:18:08.671497-08
2	Boot Problem	Computer fails to boot.	2017-11-17 23:18:37.439893-08	2017-11-17 23:18:37.439893-08
3	Hardware Failure	Asset is exhibiting issues related to hardware failure (specify in notes).	2017-11-17 23:19:34.414854-08	2017-11-17 23:19:34.415832-08
\.


--
-- TOC entry 2964 (class 0 OID 0)
-- Dependencies: 234
-- Name: rttApp_categories_id_seq; Type: SEQUENCE SET; Schema: public; Owner: django-app-client
--

SELECT pg_catalog.setval('"rttApp_categories_id_seq"', 3, true);


-- Completed on 2017-11-19 00:51:51

--
-- PostgreSQL database dump complete
--

