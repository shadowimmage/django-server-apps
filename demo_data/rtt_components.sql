--
-- PostgreSQL database dump
--

-- Dumped from database version 10.1
-- Dumped by pg_dump version 10.1

-- Started on 2017-11-19 00:52:19

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
-- TOC entry 2958 (class 0 OID 16752)
-- Dependencies: 237
-- Data for Name: rttApp_components; Type: TABLE DATA; Schema: public; Owner: django-app-client
--

COPY "rttApp_components" (id, serial, notes, date_created, date_updated, model_id) FROM stdin;
1	S124552345254GDX		2017-11-17 23:20:40.080274-08	2017-11-17 23:20:40.080274-08	4
2	S124554545254GDX		2017-11-17 23:21:06.308547-08	2017-11-17 23:21:06.308547-08	4
3	S121234565254GDX		2017-11-17 23:21:28.310132-08	2017-11-17 23:21:28.310132-08	4
\.


--
-- TOC entry 2963 (class 0 OID 0)
-- Dependencies: 236
-- Name: rttApp_components_id_seq; Type: SEQUENCE SET; Schema: public; Owner: django-app-client
--

SELECT pg_catalog.setval('"rttApp_components_id_seq"', 3, true);


-- Completed on 2017-11-19 00:52:19

--
-- PostgreSQL database dump complete
--

