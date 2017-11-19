--
-- PostgreSQL database dump
--

-- Dumped from database version 10.1
-- Dumped by pg_dump version 10.1

-- Started on 2017-11-19 00:41:14

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
-- TOC entry 2959 (class 0 OID 16552)
-- Dependencies: 215
-- Data for Name: keysApp_affiliations; Type: TABLE DATA; Schema: public; Owner: django-app-client
--

COPY "keysApp_affiliations" (id, affiliation, customer_user_id_reqd, date_added, date_updated) FROM stdin;
1	Staff	t	2017-11-17 22:39:01.680876-08	2017-11-17 22:39:01.680876-08
3	Contractor	f	2017-11-17 22:39:15.870009-08	2017-11-17 22:39:15.870009-08
4	Administrative	t	2017-11-17 22:39:30.845719-08	2017-11-17 22:39:30.845719-08
5	Customer	t	2017-11-17 22:40:25.152927-08	2017-11-17 22:40:25.152927-08
\.


--
-- TOC entry 2964 (class 0 OID 0)
-- Dependencies: 214
-- Name: keysApp_affiliations_id_seq; Type: SEQUENCE SET; Schema: public; Owner: django-app-client
--

SELECT pg_catalog.setval('"keysApp_affiliations_id_seq"', 5, true);


-- Completed on 2017-11-19 00:41:15

--
-- PostgreSQL database dump complete
--

