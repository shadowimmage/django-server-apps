--
-- PostgreSQL database dump
--

-- Dumped from database version 10.1
-- Dumped by pg_dump version 10.1

-- Started on 2017-11-19 00:53:31

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
-- TOC entry 2959 (class 0 OID 16781)
-- Dependencies: 243
-- Data for Name: rttApp_states; Type: TABLE DATA; Schema: public; Owner: django-app-client
--

COPY "rttApp_states" (id, state, description, date_created, date_updated) FROM stdin;
1	New	Issue has not been looked at yet	2017-11-17 23:22:16.377768-08	2017-11-17 23:22:16.377768-08
2	In Progress	Issue is being addressed	2017-11-17 23:22:26.350091-08	2017-11-17 23:22:26.350091-08
3	Stalled	Issue resolution is being blocked by some other issue or task	2017-11-17 23:22:51.375785-08	2017-11-17 23:22:51.375785-08
4	Resolved	Issue has been resolved / closed	2017-11-17 23:23:06.876446-08	2017-11-17 23:23:06.876446-08
\.


--
-- TOC entry 2964 (class 0 OID 0)
-- Dependencies: 242
-- Name: rttApp_states_id_seq; Type: SEQUENCE SET; Schema: public; Owner: django-app-client
--

SELECT pg_catalog.setval('"rttApp_states_id_seq"', 4, true);


-- Completed on 2017-11-19 00:53:31

--
-- PostgreSQL database dump complete
--

