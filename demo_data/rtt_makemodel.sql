--
-- PostgreSQL database dump
--

-- Dumped from database version 10.1
-- Dumped by pg_dump version 10.1

-- Started on 2017-11-19 00:52:41

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
-- TOC entry 2962 (class 0 OID 16763)
-- Dependencies: 239
-- Data for Name: rttApp_makemodel; Type: TABLE DATA; Schema: public; Owner: django-app-client
--

COPY "rttApp_makemodel" (id, model_name, description, date_created, date_updated, make_id) FROM stdin;
1	Optiplex 9020	Desktop Computer	2017-11-17 23:13:57.200802-08	2017-11-17 23:13:57.200802-08	1
2	Surface Pro 4	Tablet Computer	2017-11-17 23:15:34.435763-08	2017-11-17 23:15:34.435763-08	2
3	ZenBook	Laptop	2017-11-17 23:16:53.407976-08	2017-11-17 23:16:53.407976-08	3
4	840 EVO SSD 250GB	250GB SATA SSD	2017-11-17 23:20:29.032702-08	2017-11-17 23:20:29.032702-08	4
\.


--
-- TOC entry 2967 (class 0 OID 0)
-- Dependencies: 238
-- Name: rttApp_makemodel_id_seq; Type: SEQUENCE SET; Schema: public; Owner: django-app-client
--

SELECT pg_catalog.setval('"rttApp_makemodel_id_seq"', 4, true);


-- Completed on 2017-11-19 00:52:41

--
-- PostgreSQL database dump complete
--

