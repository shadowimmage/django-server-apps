--
-- PostgreSQL database dump
--

-- Dumped from database version 10.1
-- Dumped by pg_dump version 10.1

-- Started on 2017-11-19 00:48:21

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
-- TOC entry 2963 (class 0 OID 16606)
-- Dependencies: 225
-- Data for Name: keysApp_loanexceptions; Type: TABLE DATA; Schema: public; Owner: django-app-client
--

COPY "keysApp_loanexceptions" (id, date_expires, "limit", granted_by, admin_comment, date_added, date_updated, customer_id, key_type_id) FROM stdin;
1	2020-01-01	2	Chase Sawyer	This person can have as many QE34s as they want, as long as that is at most 2.	2017-11-17 23:11:19.203892-08	2017-11-17 23:11:19.203892-08	1	1
\.


--
-- TOC entry 2968 (class 0 OID 0)
-- Dependencies: 224
-- Name: keysApp_loanexceptions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: django-app-client
--

SELECT pg_catalog.setval('"keysApp_loanexceptions_id_seq"', 1, true);


-- Completed on 2017-11-19 00:48:21

--
-- PostgreSQL database dump complete
--

