--
-- PostgreSQL database dump
--

-- Dumped from database version 10.1
-- Dumped by pg_dump version 10.1

-- Started on 2017-11-19 00:49:12

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
-- TOC entry 2971 (class 0 OID 16629)
-- Dependencies: 229
-- Data for Name: keysApp_records; Type: TABLE DATA; Schema: public; Owner: django-app-client
--

COPY "keysApp_records" (id, date_out, date_due, extensions, date_returned, is_returned, is_overdue, number_reminders_sent, date_email_reminder_sent, is_lost_broken, date_paid_for, payment_notes, admin_comment, date_added, date_updated, customer_id, key_id, loan_term_id) FROM stdin;
1	2017-11-17 23:12:12-08	2017-12-18 22:00:00-08	0	\N	f	f	0	\N	f	\N			2017-11-17 23:12:48.994397-08	2017-11-17 23:12:48.994397-08	1	1	2
\.


--
-- TOC entry 2976 (class 0 OID 0)
-- Dependencies: 228
-- Name: keysApp_records_id_seq; Type: SEQUENCE SET; Schema: public; Owner: django-app-client
--

SELECT pg_catalog.setval('"keysApp_records_id_seq"', 1, true);


-- Completed on 2017-11-19 00:49:12

--
-- PostgreSQL database dump complete
--

