--
-- PostgreSQL database dump
--

-- Dumped from database version 10.1
-- Dumped by pg_dump version 10.1

-- Started on 2017-11-19 00:46:58

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
-- TOC entry 2965 (class 0 OID 16583)
-- Dependencies: 221
-- Data for Name: keysApp_keys; Type: TABLE DATA; Schema: public; Owner: django-app-client
--

COPY "keysApp_keys" (id, number, is_retired, retirement_type, retirement_comment, date_added, date_updated, key_type_id) FROM stdin;
1	1	f	\N		2017-11-17 23:03:13.592974-08	2017-11-17 23:03:13.592974-08	1
2	2	f	\N		2017-11-17 23:03:16.374737-08	2017-11-17 23:03:16.374737-08	1
3	3	f	\N		2017-11-17 23:03:19.232831-08	2017-11-17 23:03:19.232831-08	1
4	4	f	\N		2017-11-17 23:03:22.454937-08	2017-11-17 23:03:22.454937-08	1
5	114	f	\N		2017-11-17 23:03:27.439434-08	2017-11-17 23:03:27.439434-08	2
6	4147	f	\N		2017-11-17 23:03:33.95391-08	2017-11-17 23:03:33.95391-08	2
7	1410	f	\N		2017-11-17 23:03:37.212002-08	2017-11-17 23:03:37.212002-08	2
8	4144	f	\N		2017-11-17 23:03:44.406224-08	2017-11-17 23:03:44.406224-08	2
9	4102	f	\N		2017-11-17 23:03:49.09642-08	2017-11-17 23:03:49.09642-08	2
10	527	f	\N		2017-11-17 23:03:52.208857-08	2017-11-17 23:03:52.208857-08	2
11	1	f	\N		2017-11-17 23:03:56.813582-08	2017-11-17 23:03:56.813582-08	3
12	5	f	\N		2017-11-17 23:04:00.793832-08	2017-11-17 23:04:00.793832-08	3
13	7	f	\N		2017-11-17 23:04:04.448927-08	2017-11-17 23:04:04.448927-08	3
14	9	f	\N		2017-11-17 23:04:07.337439-08	2017-11-17 23:04:07.337439-08	3
20	2	f	\N		2017-11-17 23:04:27.593933-08	2017-11-17 23:04:27.593933-08	5
21	1	f	\N		2017-11-17 23:04:30.31249-08	2017-11-17 23:04:30.31249-08	6
22	4	f	\N		2017-11-17 23:04:33.71186-08	2017-11-17 23:04:33.71186-08	6
23	21	f	\N		2017-11-17 23:04:40.392317-08	2017-11-17 23:04:40.392317-08	5
18	4	t	1	At the bottom of a well	2017-11-17 23:04:20.417945-08	2017-11-17 23:05:01.371337-08	5
15	45	t	2	Stockroom 2 no longer exists	2017-11-17 23:04:10.736791-08	2017-11-17 23:05:32.848468-08	4
16	41	t	2	Stockroom 2 no longer exists	2017-11-17 23:04:13.526578-08	2017-11-17 23:09:01.284079-08	4
17	14	t	2	Stockroom 2 no longer exists	2017-11-17 23:04:16.936866-08	2017-11-17 23:09:17.610032-08	4
19	4	t	2	Stockroom 2 no longer exists	2017-11-17 23:04:23.846412-08	2017-11-17 23:09:24.584341-08	4
\.


--
-- TOC entry 2970 (class 0 OID 0)
-- Dependencies: 220
-- Name: keysApp_keys_id_seq; Type: SEQUENCE SET; Schema: public; Owner: django-app-client
--

SELECT pg_catalog.setval('"keysApp_keys_id_seq"', 23, true);


-- Completed on 2017-11-19 00:46:58

--
-- PostgreSQL database dump complete
--

