--
-- PostgreSQL database dump
--

-- Dumped from database version 10.1
-- Dumped by pg_dump version 10.1

-- Started on 2017-11-19 00:45:51

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
-- TOC entry 2960 (class 0 OID 16572)
-- Dependencies: 219
-- Data for Name: keysApp_departments; Type: TABLE DATA; Schema: public; Owner: django-app-client
--

COPY "keysApp_departments" (id, dept_name, box_number, admin_name, admin_contact, date_updated, date_added) FROM stdin;
1	Facilities	443588	Marcus Aloisi	maloisi@djangosite.demo	2017-11-17 22:44:11.519554-08	2017-11-17 22:43:34.446465-08
2	Security Services	406541	Mike Zupan	1231234567	2017-11-17 22:50:01.83214-08	2017-11-17 22:50:01.83214-08
3	Nomail Services	132413			2017-11-17 22:53:09.798484-08	2017-11-17 22:53:09.798484-08
4	KeysApp Admin	0			2017-11-17 22:54:51.369304-08	2017-11-17 22:54:42.598887-08
5	Jerrymandering Dept	541324			2017-11-17 22:57:32.173095-08	2017-11-17 22:57:32.173095-08
6	Totally Legitimate Industries	231324	Leonard Wang	email	2017-11-17 23:00:07.14931-08	2017-11-17 23:00:07.14931-08
\.


--
-- TOC entry 2965 (class 0 OID 0)
-- Dependencies: 218
-- Name: keysApp_departments_id_seq; Type: SEQUENCE SET; Schema: public; Owner: django-app-client
--

SELECT pg_catalog.setval('"keysApp_departments_id_seq"', 6, true);


-- Completed on 2017-11-19 00:45:51

--
-- PostgreSQL database dump complete
--

