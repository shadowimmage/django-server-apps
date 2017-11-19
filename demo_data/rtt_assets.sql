--
-- PostgreSQL database dump
--

-- Dumped from database version 10.1
-- Dumped by pg_dump version 10.1

-- Started on 2017-11-19 00:51:10

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
-- TOC entry 2968 (class 0 OID 16723)
-- Dependencies: 233
-- Data for Name: rttApp_assets; Type: TABLE DATA; Schema: public; Owner: django-app-client
--

COPY "rttApp_assets" (id, number, serial, description, mac_address, notes, date_created, date_updated, model_id) FROM stdin;
1	1125	AFKJVBLD234RF24		AC:34:DE:31:12:44		2017-11-17 23:14:27.891501-08	2017-11-17 23:14:27.891501-08	1
2	1124	DSFVBNUILFDV4232		AF:12:34:45:12:DC		2017-11-17 23:14:57.752263-08	2017-11-17 23:14:57.752263-08	1
3	1122	5231354334FDSG		12:35:46:87:39:DD		2017-11-17 23:16:07.729949-08	2017-11-17 23:16:07.729949-08	2
4	42	822398900	This is probably a laptop.	aa:bb:cc:11:22:33	Has never been seen.	2017-11-17 23:17:30.38104-08	2017-11-17 23:17:30.38104-08	3
\.


--
-- TOC entry 2973 (class 0 OID 0)
-- Dependencies: 232
-- Name: rttApp_assets_id_seq; Type: SEQUENCE SET; Schema: public; Owner: django-app-client
--

SELECT pg_catalog.setval('"rttApp_assets_id_seq"', 4, true);


-- Completed on 2017-11-19 00:51:10

--
-- PostgreSQL database dump complete
--

