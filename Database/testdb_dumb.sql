--
-- PostgreSQL database dump
--

-- Dumped from database version 16.8
-- Dumped by pg_dump version 16.8

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: data_advantages; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.data_advantages (
    id integer NOT NULL,
    aspect character varying(100) NOT NULL,
    value character varying(50) NOT NULL
);


ALTER TABLE public.data_advantages OWNER TO postgres;

--
-- Name: data_advantages_advantages_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.data_advantages_advantages_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.data_advantages_advantages_id_seq OWNER TO postgres;

--
-- Name: data_advantages_advantages_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.data_advantages_advantages_id_seq OWNED BY public.data_advantages.id;


--
-- Name: data_disadvantages; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.data_disadvantages (
    id integer NOT NULL,
    aspect character varying(100) NOT NULL,
    value character varying(50) NOT NULL
);


ALTER TABLE public.data_disadvantages OWNER TO postgres;

--
-- Name: data_disadvantages_disadvantages_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.data_disadvantages_disadvantages_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.data_disadvantages_disadvantages_id_seq OWNER TO postgres;

--
-- Name: data_disadvantages_disadvantages_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.data_disadvantages_disadvantages_id_seq OWNED BY public.data_disadvantages.id;


--
-- Name: data_european_comparation; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.data_european_comparation (
    id integer NOT NULL,
    aspect character varying(100) NOT NULL,
    value character varying(50) NOT NULL
);


ALTER TABLE public.data_european_comparation OWNER TO postgres;

--
-- Name: data_european_comparation_european_comparation_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.data_european_comparation_european_comparation_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.data_european_comparation_european_comparation_id_seq OWNER TO postgres;

--
-- Name: data_european_comparation_european_comparation_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.data_european_comparation_european_comparation_id_seq OWNED BY public.data_european_comparation.id;


--
-- Name: data_general; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.data_general (
    id integer NOT NULL,
    aspect character varying(100) NOT NULL,
    value character varying(50) NOT NULL
);


ALTER TABLE public.data_general OWNER TO postgres;

--
-- Name: data_general_general_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.data_general_general_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.data_general_general_id_seq OWNER TO postgres;

--
-- Name: data_general_general_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.data_general_general_id_seq OWNED BY public.data_general.id;


--
-- Name: data_men; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.data_men (
    id integer NOT NULL,
    aspect character varying(100) NOT NULL,
    value character varying(50) NOT NULL
);


ALTER TABLE public.data_men OWNER TO postgres;

--
-- Name: data_men_men_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.data_men_men_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.data_men_men_id_seq OWNER TO postgres;

--
-- Name: data_men_men_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.data_men_men_id_seq OWNED BY public.data_men.id;


--
-- Name: data_special; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.data_special (
    id integer NOT NULL,
    aspect character varying(100) NOT NULL,
    value character varying(50) NOT NULL
);


ALTER TABLE public.data_special OWNER TO postgres;

--
-- Name: data_special_special_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.data_special_special_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.data_special_special_id_seq OWNER TO postgres;

--
-- Name: data_special_special_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.data_special_special_id_seq OWNED BY public.data_special.id;


--
-- Name: users; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.users (
    id integer NOT NULL,
    username text NOT NULL,
    password_hash text NOT NULL
);


ALTER TABLE public.users OWNER TO postgres;

--
-- Name: users_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.users_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.users_id_seq OWNER TO postgres;

--
-- Name: users_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.users_id_seq OWNED BY public.users.id;


--
-- Name: video_source; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.video_source (
    id integer NOT NULL,
    video_source character varying(100) NOT NULL
);


ALTER TABLE public.video_source OWNER TO postgres;

--
-- Name: data_advantages id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.data_advantages ALTER COLUMN id SET DEFAULT nextval('public.data_advantages_advantages_id_seq'::regclass);


--
-- Name: data_disadvantages id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.data_disadvantages ALTER COLUMN id SET DEFAULT nextval('public.data_disadvantages_disadvantages_id_seq'::regclass);


--
-- Name: data_european_comparation id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.data_european_comparation ALTER COLUMN id SET DEFAULT nextval('public.data_european_comparation_european_comparation_id_seq'::regclass);


--
-- Name: data_general id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.data_general ALTER COLUMN id SET DEFAULT nextval('public.data_general_general_id_seq'::regclass);


--
-- Name: data_men id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.data_men ALTER COLUMN id SET DEFAULT nextval('public.data_men_men_id_seq'::regclass);


--
-- Name: data_special id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.data_special ALTER COLUMN id SET DEFAULT nextval('public.data_special_special_id_seq'::regclass);


--
-- Name: users id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.users ALTER COLUMN id SET DEFAULT nextval('public.users_id_seq'::regclass);


--
-- Data for Name: data_advantages; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.data_advantages (id, aspect, value) FROM stdin;
0	Zeitgewinn durch Wegfall des Arbeitsweges	76%
1	Bessere Vereinbarkeit von Beruf und Familie	73%
2	freie Arbeitszeiteinteilung	68%
3	produktivere Arbeitsphasen als im Büro	63%
4	Angenehmere Arbeit generell	61%
\.


--
-- Data for Name: data_disadvantages; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.data_disadvantages (id, aspect, value) FROM stdin;
0	Fehlender Kontakt zu Kollegen	74%
1	Fehlende Trennung von Beruf und Privatleben	45%
2	Beeinträchtigung der Arbeit durch fehlenden Kontakt	39%
3	Erschwerter Zugang zu Unterlagen im Homeoffice	35%
\.


--
-- Data for Name: data_european_comparation; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.data_european_comparation (id, aspect, value) FROM stdin;
0	Deutschland	5%
1	Dänemark	14%
2	Belgien	11%
3	Östereich	10%
4	Frankreich	6,6%
5	Irland	6,5%
6	Spanien	4,3%
7	Italien	3,6%
9	Mosambik	5,24
8	Luxemburg	54%
\.


--
-- Data for Name: data_general; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.data_general (id, aspect, value) FROM stdin;
0	Wachstum der Remote Arbeitenden seit 2009	159%
1	Anteil der in Deutschland remote arbeitenden Angestellten	24%
2	Anteil der weltweit vollständig remote arbeitenden	16%
3	Anteil der Befragten, die im Homeoffice produktiver sind als im Büro	77%
4	Anzahl an Autos, um die durch Homeoffice Abgasemissionen eingespart wird	600.000
5	Bis 2028 sind global Remote-Arbeiter	73%
6	Stimmen für einen gesetzlichen Anspruch auf Homeoffice	73%
7	Favorisieren Homeoffice aufgrund fehlender Ablenkung	75%
8	Jährliche Gesamtsumme, die Angestellte im Homeoffice für Transport, Essen und Kinderbetreuung sparen	7000$
\.


--
-- Data for Name: data_men; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.data_men (id, aspect, value) FROM stdin;
0	Nutzen zumindest teilweise eine Form des mobilen Arbeitens	31%
1	Davon im Büro bei einem Vollzeit Job	70%
2	Davon im Büro bei einem Teilzeit Job	56%
3	Männer, die prinzipiell kein Homeoffice machen wollen	2%
\.


--
-- Data for Name: data_special; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.data_special (id, aspect, value) FROM stdin;
1	Arbeiten auf Geschäftsreisen mobil	19%
2	Nutzen das Homeoffice als mobile Arbeitsform	18%
3	Arbeiten von verschiedenen Gesschäftstandorten aus	15%
4	Nutzen öffentliche Orte als Arbeitsplatz	4%
5	Gehen in selbst angemieteten Räumen Homeoffice nach	0,3%
0	Arbeiten beim Kunden vor Ort	22%
\.


--
-- Data for Name: users; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.users (id, username, password_hash) FROM stdin;
\.


--
-- Data for Name: video_source; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.video_source (id, video_source) FROM stdin;
\.


--
-- Name: data_advantages_advantages_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.data_advantages_advantages_id_seq', 1, false);


--
-- Name: data_disadvantages_disadvantages_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.data_disadvantages_disadvantages_id_seq', 1, false);


--
-- Name: data_european_comparation_european_comparation_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.data_european_comparation_european_comparation_id_seq', 1, false);


--
-- Name: data_general_general_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.data_general_general_id_seq', 13, true);


--
-- Name: data_men_men_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.data_men_men_id_seq', 1, false);


--
-- Name: data_special_special_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.data_special_special_id_seq', 1, false);


--
-- Name: users_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.users_id_seq', 1, false);


--
-- Name: data_advantages data_advantages_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.data_advantages
    ADD CONSTRAINT data_advantages_pkey PRIMARY KEY (id);


--
-- Name: data_disadvantages data_disadvantages_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.data_disadvantages
    ADD CONSTRAINT data_disadvantages_pkey PRIMARY KEY (id);


--
-- Name: data_european_comparation data_european_comparation_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.data_european_comparation
    ADD CONSTRAINT data_european_comparation_pkey PRIMARY KEY (id);


--
-- Name: data_general data_general_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.data_general
    ADD CONSTRAINT data_general_pkey PRIMARY KEY (id);


--
-- Name: data_men data_men_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.data_men
    ADD CONSTRAINT data_men_pkey PRIMARY KEY (id);


--
-- Name: data_special data_special_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.data_special
    ADD CONSTRAINT data_special_pkey PRIMARY KEY (id);


--
-- Name: users users_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_pkey PRIMARY KEY (id);


--
-- Name: users users_username_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_username_key UNIQUE (username);


--
-- Name: video_source video_source_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.video_source
    ADD CONSTRAINT video_source_pkey PRIMARY KEY (id);


--
-- PostgreSQL database dump complete
--

