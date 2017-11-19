--
-- PostgreSQL database dump
--

-- Dumped from database version 10.1
-- Dumped by pg_dump version 10.1

-- Started on 2017-11-19 00:48:47

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
-- TOC entry 2962 (class 0 OID 16618)
-- Dependencies: 227
-- Data for Name: keysApp_loanterms; Type: TABLE DATA; Schema: public; Owner: django-app-client
--

COPY "keysApp_loanterms" (id, term_desc, term_length, date_added, date_updated) FROM stdin;
1	Short Term	7	2017-11-17 23:09:50.60914-08	2017-11-17 23:09:50.60914-08
2	Long Term	31	2017-11-17 23:09:56.886065-08	2017-11-17 23:09:56.886065-08
\.


--
-- TOC entry 2967 (class 0 OID 0)
-- Dependencies: 226
-- Name: keysApp_loanterms_id_seq; Type: SEQUENCE SET; Schema: public; Owner: django-app-client
--

SELECT pg_catalog.setval('"keysApp_loanterms_id_seq"', 2, true);


-- Completed on 2017-11-19 00:48:47

--
-- PostgreSQL database dump complete
--

