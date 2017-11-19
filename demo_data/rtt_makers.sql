--
-- PostgreSQL database dump
--

-- Dumped from database version 10.1
-- Dumped by pg_dump version 10.1

-- Started on 2017-11-19 00:52:59

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
-- TOC entry 2959 (class 0 OID 16771)
-- Dependencies: 241
-- Data for Name: rttApp_makers; Type: TABLE DATA; Schema: public; Owner: django-app-client
--

COPY "rttApp_makers" (id, maker, date_created, date_updated) FROM stdin;
1	Dell	2017-11-17 23:13:42.867026-08	2017-11-17 23:13:42.867026-08
2	Microsoft	2017-11-17 23:15:15.382831-08	2017-11-17 23:15:15.382831-08
3	Asus	2017-11-17 23:16:26.942122-08	2017-11-17 23:16:26.942122-08
4	Samsung	2017-11-17 23:19:48.001281-08	2017-11-17 23:19:48.001281-08
\.


--
-- TOC entry 2964 (class 0 OID 0)
-- Dependencies: 240
-- Name: rttApp_makers_id_seq; Type: SEQUENCE SET; Schema: public; Owner: django-app-client
--

SELECT pg_catalog.setval('"rttApp_makers_id_seq"', 4, true);


-- Completed on 2017-11-19 00:52:59

--
-- PostgreSQL database dump complete
--

