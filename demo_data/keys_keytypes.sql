--
-- PostgreSQL database dump
--

-- Dumped from database version 10.1
-- Dumped by pg_dump version 10.1

-- Started on 2017-11-19 00:47:28

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
-- TOC entry 2959 (class 0 OID 16596)
-- Dependencies: 223
-- Data for Name: keysApp_keytypes; Type: TABLE DATA; Schema: public; Owner: django-app-client
--

COPY "keysApp_keytypes" (id, key_type, description, date_added, date_updated) FROM stdin;
1	QE34	South Entrance Doors	2017-11-17 23:00:44.749898-08	2017-11-17 23:00:44.749898-08
2	Q7AB2	North doors	2017-11-17 23:01:19.099106-08	2017-11-17 23:01:19.099106-08
3	IUFH-M	Stockroom Master	2017-11-17 23:02:04.516996-08	2017-11-17 23:02:04.516996-08
4	IUFH-S	Stockroom 2	2017-11-17 23:02:24.592278-08	2017-11-17 23:02:24.592278-08
5	IUFH-W	Stockroom 1	2017-11-17 23:02:37.078935-08	2017-11-17 23:02:37.078935-08
6	IUFH-99	Stockroom 3	2017-11-17 23:02:56.494935-08	2017-11-17 23:02:56.494935-08
\.


--
-- TOC entry 2964 (class 0 OID 0)
-- Dependencies: 222
-- Name: keysApp_keytypes_id_seq; Type: SEQUENCE SET; Schema: public; Owner: django-app-client
--

SELECT pg_catalog.setval('"keysApp_keytypes_id_seq"', 6, true);


-- Completed on 2017-11-19 00:47:28

--
-- PostgreSQL database dump complete
--

