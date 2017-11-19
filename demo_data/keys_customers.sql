--
-- PostgreSQL database dump
--

-- Dumped from database version 10.1
-- Dumped by pg_dump version 10.1

-- Started on 2017-11-19 00:44:14

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
-- TOC entry 2967 (class 0 OID 16562)
-- Dependencies: 217
-- Data for Name: keysApp_customers; Type: TABLE DATA; Schema: public; Owner: django-app-client
--

COPY "keysApp_customers" (id, user_id, last_name, first_name, phone_number, email_address, email_is_bad, date_added, date_updated, affiliation_id, department_id) FROM stdin;
1	crusty	Marcus	Aloisi	1234567890	maloisi@djangosite.demo	f	2017-11-17 22:44:13.447809-08	2017-11-17 22:44:13.447809-08	1	1
2	tawdry	Garner	Iris	1234567890	igarner@djangosite.demo	f	2017-11-17 22:46:23.956438-08	2017-11-17 22:46:23.956438-08	1	1
3	grotesque	Noel	Nevena	1234567890	nnoel@djangosite.demo	f	2017-11-17 22:47:09.790404-08	2017-11-17 22:47:09.791408-08	1	1
4	piquant	Zupan	Mike	1231234567	mzupan@djangosite.demo	f	2017-11-17 22:50:05.233588-08	2017-11-17 22:50:05.233588-08	3	2
5	\N	Boucher	Walery	1234561234	walery.boucher@nomail.org	f	2017-11-17 22:53:12.33075-08	2017-11-17 22:53:12.33075-08	3	3
6	eclipse	Pascal	Becke	5-4556	BPascal@keysapp.com	f	2017-11-17 22:54:55.304082-08	2017-11-17 22:54:55.304082-08	4	4
7	hyperion	Francis	Courtney	5-1347	CFrancis@keysapp.com	f	2017-11-17 22:55:49.968282-08	2017-11-17 22:55:49.968282-08	4	4
8	coconut	Irwin	Casper	1234567890	cirwin@customer.site	f	2017-11-17 22:57:35.275292-08	2017-11-17 22:57:35.275292-08	5	5
9	quiche	Bodilsen	Conrad	1234567894	cbodilsen@customer.site	f	2017-11-17 22:58:32.29077-08	2017-11-17 22:58:32.29077-08	5	5
10	garlic	Wang	Leonardo	1111111111	lwang@customer.site	f	2017-11-17 23:00:08.715956-08	2017-11-17 23:00:08.715956-08	5	6
\.


--
-- TOC entry 2972 (class 0 OID 0)
-- Dependencies: 216
-- Name: keysApp_customers_id_seq; Type: SEQUENCE SET; Schema: public; Owner: django-app-client
--

SELECT pg_catalog.setval('"keysApp_customers_id_seq"', 10, true);


-- Completed on 2017-11-19 00:44:14

--
-- PostgreSQL database dump complete
--

