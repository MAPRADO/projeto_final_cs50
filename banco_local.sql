--
-- PostgreSQL database dump
--

-- Dumped from database version 15.8
-- Dumped by pg_dump version 15.8

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

--
-- Name: adminpack; Type: EXTENSION; Schema: -; Owner: -
--

CREATE EXTENSION IF NOT EXISTS adminpack WITH SCHEMA pg_catalog;


--
-- Name: EXTENSION adminpack; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION adminpack IS 'administrative functions for PostgreSQL';


SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: advantage; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.advantage (
    id_advantage integer NOT NULL,
    alcohol_value real NOT NULL,
    gasoline_value real NOT NULL,
    advantage character varying(255) NOT NULL,
    id_name integer NOT NULL
);


ALTER TABLE public.advantage OWNER TO postgres;

--
-- Name: advantage_id_advantage_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.advantage_id_advantage_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.advantage_id_advantage_seq OWNER TO postgres;

--
-- Name: advantage_id_advantage_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.advantage_id_advantage_seq OWNED BY public.advantage.id_advantage;


--
-- Name: advantage_id_name_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.advantage_id_name_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.advantage_id_name_seq OWNER TO postgres;

--
-- Name: advantage_id_name_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.advantage_id_name_seq OWNED BY public.advantage.id_name;


--
-- Name: name; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.name (
    id integer NOT NULL,
    user_name character varying(255) NOT NULL,
    car_brand character varying(255) NOT NULL,
    model character varying(255) NOT NULL,
    motor real NOT NULL
);


ALTER TABLE public.name OWNER TO postgres;

--
-- Name: name_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.name_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.name_id_seq OWNER TO postgres;

--
-- Name: name_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.name_id_seq OWNED BY public.name.id;


--
-- Name: advantage id_advantage; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.advantage ALTER COLUMN id_advantage SET DEFAULT nextval('public.advantage_id_advantage_seq'::regclass);


--
-- Name: advantage id_name; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.advantage ALTER COLUMN id_name SET DEFAULT nextval('public.advantage_id_name_seq'::regclass);


--
-- Name: name id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.name ALTER COLUMN id SET DEFAULT nextval('public.name_id_seq'::regclass);


--
-- Data for Name: advantage; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.advantage (id_advantage, alcohol_value, gasoline_value, advantage, id_name) FROM stdin;
\.


--
-- Data for Name: name; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.name (id, user_name, car_brand, model, motor) FROM stdin;
\.


--
-- Name: advantage_id_advantage_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.advantage_id_advantage_seq', 1, false);


--
-- Name: advantage_id_name_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.advantage_id_name_seq', 1, false);


--
-- Name: name_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.name_id_seq', 1, false);


--
-- Name: advantage advantage_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.advantage
    ADD CONSTRAINT advantage_pkey PRIMARY KEY (id_advantage);


--
-- Name: name name_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.name
    ADD CONSTRAINT name_pkey PRIMARY KEY (id);


--
-- Name: advantage advantage_id_name_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.advantage
    ADD CONSTRAINT advantage_id_name_fkey FOREIGN KEY (id_name) REFERENCES public.name(id);


--
-- PostgreSQL database dump complete
--

