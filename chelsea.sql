--
-- PostgreSQL database dump
--

SET statement_timeout = 0;
SET lock_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SET check_function_bodies = false;
SET client_min_messages = warning;

--
-- Name: plpgsql; Type: EXTENSION; Schema: -; Owner: 
--

CREATE EXTENSION IF NOT EXISTS plpgsql WITH SCHEMA pg_catalog;


--
-- Name: EXTENSION plpgsql; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION plpgsql IS 'PL/pgSQL procedural language';


SET search_path = public, pg_catalog;

SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: categories; Type: TABLE; Schema: public; Owner: user; Tablespace: 
--

CREATE TABLE categories (
    category_id integer NOT NULL,
    category_name character varying(100) NOT NULL
);


ALTER TABLE public.categories OWNER TO "user";

--
-- Name: categories_category_id_seq; Type: SEQUENCE; Schema: public; Owner: user
--

CREATE SEQUENCE categories_category_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.categories_category_id_seq OWNER TO "user";

--
-- Name: categories_category_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: user
--

ALTER SEQUENCE categories_category_id_seq OWNED BY categories.category_id;


--
-- Name: images; Type: TABLE; Schema: public; Owner: user; Tablespace: 
--

CREATE TABLE images (
    image_id integer NOT NULL,
    image_common_name character varying(100) NOT NULL
);


ALTER TABLE public.images OWNER TO "user";

--
-- Name: images_image_id_seq; Type: SEQUENCE; Schema: public; Owner: user
--

CREATE SEQUENCE images_image_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.images_image_id_seq OWNER TO "user";

--
-- Name: images_image_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: user
--

ALTER SEQUENCE images_image_id_seq OWNED BY images.image_id;


--
-- Name: poses; Type: TABLE; Schema: public; Owner: user; Tablespace: 
--

CREATE TABLE poses (
    pose_id integer NOT NULL,
    category character varying(100),
    common_name character varying(100) NOT NULL,
    sanskrit_name character varying(100),
    breathe character varying(500),
    image_url character varying(500),
    "time" integer,
    pregnancy integer
);


ALTER TABLE public.poses OWNER TO "user";

--
-- Name: poses_pose_id_seq; Type: SEQUENCE; Schema: public; Owner: user
--

CREATE SEQUENCE poses_pose_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.poses_pose_id_seq OWNER TO "user";

--
-- Name: poses_pose_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: user
--

ALTER SEQUENCE poses_pose_id_seq OWNED BY poses.pose_id;


--
-- Name: sequences; Type: TABLE; Schema: public; Owner: user; Tablespace: 
--

CREATE TABLE sequences (
    seq_id integer NOT NULL,
    user_id integer,
    seq_name character varying(500),
    poses integer[]
);


ALTER TABLE public.sequences OWNER TO "user";

--
-- Name: sequences_seq_id_seq; Type: SEQUENCE; Schema: public; Owner: user
--

CREATE SEQUENCE sequences_seq_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.sequences_seq_id_seq OWNER TO "user";

--
-- Name: sequences_seq_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: user
--

ALTER SEQUENCE sequences_seq_id_seq OWNED BY sequences.seq_id;


--
-- Name: users; Type: TABLE; Schema: public; Owner: user; Tablespace: 
--

CREATE TABLE users (
    user_id integer NOT NULL,
    email character varying(64),
    password character varying(64)
);


ALTER TABLE public.users OWNER TO "user";

--
-- Name: users_user_id_seq; Type: SEQUENCE; Schema: public; Owner: user
--

CREATE SEQUENCE users_user_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.users_user_id_seq OWNER TO "user";

--
-- Name: users_user_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: user
--

ALTER SEQUENCE users_user_id_seq OWNED BY users.user_id;


--
-- Name: category_id; Type: DEFAULT; Schema: public; Owner: user
--

ALTER TABLE ONLY categories ALTER COLUMN category_id SET DEFAULT nextval('categories_category_id_seq'::regclass);


--
-- Name: image_id; Type: DEFAULT; Schema: public; Owner: user
--

ALTER TABLE ONLY images ALTER COLUMN image_id SET DEFAULT nextval('images_image_id_seq'::regclass);


--
-- Name: pose_id; Type: DEFAULT; Schema: public; Owner: user
--

ALTER TABLE ONLY poses ALTER COLUMN pose_id SET DEFAULT nextval('poses_pose_id_seq'::regclass);


--
-- Name: seq_id; Type: DEFAULT; Schema: public; Owner: user
--

ALTER TABLE ONLY sequences ALTER COLUMN seq_id SET DEFAULT nextval('sequences_seq_id_seq'::regclass);


--
-- Name: user_id; Type: DEFAULT; Schema: public; Owner: user
--

ALTER TABLE ONLY users ALTER COLUMN user_id SET DEFAULT nextval('users_user_id_seq'::regclass);


--
-- Data for Name: categories; Type: TABLE DATA; Schema: public; Owner: user
--

COPY categories (category_id, category_name) FROM stdin;
1	Spine_Strengthening_Series
2	Crescent_Lunge_Series
3	Core_Strengthening_Series
4	Namaste
5	Surrender_Series
6	Integration
7	Forward_Fold_Series
8	Intention
9	Triangle_Series
10	Balancing_Series
11	Sun_Salutation_B
12	Hip_Opener_Series
13	Sun_Salutation_A
\.


--
-- Name: categories_category_id_seq; Type: SEQUENCE SET; Schema: public; Owner: user
--

SELECT pg_catalog.setval('categories_category_id_seq', 13, true);


--
-- Data for Name: images; Type: TABLE DATA; Schema: public; Owner: user
--

COPY images (image_id, image_common_name) FROM stdin;
1	images
\.


--
-- Name: images_image_id_seq; Type: SEQUENCE SET; Schema: public; Owner: user
--

SELECT pg_catalog.setval('images_image_id_seq', 1, true);


--
-- Data for Name: poses; Type: TABLE DATA; Schema: public; Owner: user
--

COPY poses (pose_id, category, common_name, sanskrit_name, breathe, image_url, "time", pregnancy) FROM stdin;
1	Integration	Child's Pose	Balasana	Exhale	http://www.pocketyoga.com/images/poses/child_traditional.png	2	1
2	Integration	Downward Facing Dog	Adho_Mukha_Svanasana	Exhale	http://www.pocketyoga.com/images/poses/downward_dog.png	1	1
3	Integration	Ragdoll	Uttanasana	Exhale	http://www.pocketyoga.com/images/poses/forward_bend.png	1	0
4	Intention	Stand_at_Attention	Samasthiti	Exhale	http://www.pocketyoga.com/images/poses/chair_prayer.png	1	1
5	Sun Salutation A	Mountain Pose	Tadasana	2.5	http://www.pocketyoga.com/images/poses/mountain.png	1	0
6	Sun Salutation A	Standing Forward Fold	Uttanasana	2	http://www.pocketyoga.com/images/poses/forward_bend.png	1	1
7	Sun Salutation A	Halfway Lift	Ardha_Uttanasana	1.75	http://www.pocketyoga.com/images/poses/forward_bend_half_way.png	1	0
8	Sun Salutation A	High_Plank_to_Mid_Plank	Chaturanga_Dandasana	2	http://www.pocketyoga.com/images/poses/chair_prayer.png	1	1
9	Sun Salutation A	Upward Facing Dog	Urdhva_Mukha_Svanasana	2	http://www.pocketyoga.com/images/poses/upward_dog.png	1	0
10	Sun Salutation B	Table Pose		2.25	http://www.pocketyoga.com/images/poses/box_neutral.png	1	1
11	Sun Salutation B	Chair Pose	Urdhva_Mukha_Svanasana	2	http://www.pocketyoga.com/images/poses/chair.png	1	0
12	Sun Salutation B	Warrior Two	Virabhadrasana_II	2.5	http://www.pocketyoga.com/images/poses/warrior_II_R.png	1	1
13	Sun Salutation B	Extended Side Angle	Utthita_Parsvakonasana	2.5	http://www.pocketyoga.com/images/poses/warrior_II_forward_arm_forward_R.png	1	0
14	Sun Salutation B	Reverse Warrior	Utthita_Parsvakonasana	2.5	http://www.pocketyoga.com/images/poses/warrior_II_reverse_R.png	1	1
15	Core	Reclined Bound Angle Sit-Ups		2.5	http://www.pocketyoga.com/images/poses/supine_bound_angle.png	1	0
16	Core	Bicycle Sit-Ups		2.5	http://www.pocketyoga.com/images/poses/wind_removing_R.png	1	1
17	Core	Boat Pose		2.5	http://www.pocketyoga.com/images/poses/boat_full.png	1	0
18	Crescent Lunge Series	Cresent Lunge	Anjaneyasana	3	http://www.pocketyoga.com/images/poses/lunge_crescent_R.png	1	1
19	Crescent Lunge Series	Revolved Cresent Lunge	Parivrtta_Anjaneyasana	2	http://www.pocketyoga.com/images/poses/lunge_kneeling_twist_R.png	1	0
20	Crescent Lunge Series	Runner's Lunge		3	http://www.pocketyoga.com/images/poses/lunge_R.png	1	1
21	Crescent Lunge Series	Side Plank	Vasisthasana	2.5	hhttp://www.pocketyoga.com/images/poses/plank_side_L.png	1	0
22	Crescent Lunge Series	Prayer Twist	Vasisthasana	2.5	http://www.pocketyoga.com/images/poses/chair_twist_R.png	1	0
23	Crescent Lunge Series	Frog Pose		3	http://www.pocketyoga.com/images/poses/seated_on_heels_hands_on_mat_opened_knees.png	1	1
24	Crescent Lunge Series	Crow Pose	Bakasana	2.75	http://www.pocketyoga.com/images/poses/crow.png	1	0
25	Balancing Series	Eagle Pose	Garudasana	2.25	http://www.pocketyoga.com/images/poses/eagle_L.png	1	1
26	Balancing Series	Dancer's Pose	Natarajasana	4	http://www.pocketyoga.com/images/poses/lord_of_the_dance_R.png	1	1
27	Balancing Series	Warrior One	Virabhadrasana_I	3	http://www.pocketyoga.com/images/poses/warrior_I_R.png	1	0
28	Triangle Series	Triangle Pose	Trikonasana	2.5	http://www.pocketyoga.com/images/poses/triangle_forward_R.png	1	1
29	Triangle Series	Wide_Leg_Forward_Fold	Prasarita_Padottanasana	2.75	http://www.pocketyoga.com/images/poses/forward_bend_deep.png	1	0
30	Hip Opener	Half Pigeon	Eka_Pada_Rajakapotasana	2.5	http://www.pocketyoga.com/images/poses/pigeon_half_R.png	1	1
31	Spine Strengthening Series	Cobra Pose	Bhujangasana	2.75	http://www.pocketyoga.com/images/poses/cobra.png	1	0
32	Spine Strengthening Series	Floor Bow	Dhanurasana	2.5	http://www.pocketyoga.com/images/poses/bow.png	1	1
33	Spine Strengthening Series	Camel Pose	Ustrasana	2.25	http://www.pocketyoga.com/images/poses/camel.png	1	0
34	Spine Strengthening Series	Bridge Pose	Setu_Bandha_Sarvangasana	2.5	http://www.pocketyoga.com/images/poses/bridge.png	1	1
35	Spine Strengthening Series	Reclined Bound Angle Pose		2.5	http://www.pocketyoga.com/images/poses/supine_bound_angle.png	1	0
36	Forward Fold	Seated Forward Fold	Paschimottanasana	2.5	http://www.pocketyoga.com/images/poses/seated_forward_bend.png	1	1
37	Surrender Series	Happy Baby Pose	Ananda_Balasana	2.25	http://www.pocketyoga.com/images/poses/blissful_baby.png	1	0
38	Surrender Series	Supine Twist	Jathara_Parivartanasana	2.5	http://www.pocketyoga.com/images/poses/supine_spinal_twist_R.png	1	1
39	Surrender Series	Corpse_Pose	Savasana	2.5	http://www.pocketyoga.com/images/poses/corpse.png	1	0
40	Surrender Series	Namaste	The_light_in_me_honors_the_light_in_you	2.5	http://www.pocketyoga.com/images/poses/easy.png	1	0
\.


--
-- Name: poses_pose_id_seq; Type: SEQUENCE SET; Schema: public; Owner: user
--

SELECT pg_catalog.setval('poses_pose_id_seq', 40, true);


--
-- Data for Name: sequences; Type: TABLE DATA; Schema: public; Owner: user
--

COPY sequences (seq_id, user_id, seq_name, poses) FROM stdin;
1	1	breath	{1,2}
4	3	Morning salute	{1,2,6,30}
5	3	Evening	{1,2,6,30,34,35,38,39}
6	3	Evening	{1,2,6,30,34,35,38,39}
7	3	Noon	{1,2,6,30,34,35,38,39}
8	3	Energy	{29,33,37}
9	3	Morning salute	{1}
10	6	Tully 	{1,8,18,31,35}
11	6	Heart Chakra	{1,2,3}
\.


--
-- Name: sequences_seq_id_seq; Type: SEQUENCE SET; Schema: public; Owner: user
--

SELECT pg_catalog.setval('sequences_seq_id_seq', 11, true);


--
-- Data for Name: users; Type: TABLE DATA; Schema: public; Owner: user
--

COPY users (user_id, email, password) FROM stdin;
1	Chelsea@chelsea.com	 Chelsea
2	Tsegi@tsegi.com	 Tsegi
3	Sunshine@sunshine.com	 Sunshine
4	Mohamed@mohamed.com	 Mohamed
5	Chels@chels.com	Chels
6	Tully@tully.com	Tully
\.


--
-- Name: users_user_id_seq; Type: SEQUENCE SET; Schema: public; Owner: user
--

SELECT pg_catalog.setval('users_user_id_seq', 6, true);


--
-- Name: categories_pkey; Type: CONSTRAINT; Schema: public; Owner: user; Tablespace: 
--

ALTER TABLE ONLY categories
    ADD CONSTRAINT categories_pkey PRIMARY KEY (category_id);


--
-- Name: images_pkey; Type: CONSTRAINT; Schema: public; Owner: user; Tablespace: 
--

ALTER TABLE ONLY images
    ADD CONSTRAINT images_pkey PRIMARY KEY (image_id);


--
-- Name: poses_pkey; Type: CONSTRAINT; Schema: public; Owner: user; Tablespace: 
--

ALTER TABLE ONLY poses
    ADD CONSTRAINT poses_pkey PRIMARY KEY (pose_id);


--
-- Name: sequences_pkey; Type: CONSTRAINT; Schema: public; Owner: user; Tablespace: 
--

ALTER TABLE ONLY sequences
    ADD CONSTRAINT sequences_pkey PRIMARY KEY (seq_id);


--
-- Name: users_pkey; Type: CONSTRAINT; Schema: public; Owner: user; Tablespace: 
--

ALTER TABLE ONLY users
    ADD CONSTRAINT users_pkey PRIMARY KEY (user_id);


--
-- Name: sequences_user_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: user
--

ALTER TABLE ONLY sequences
    ADD CONSTRAINT sequences_user_id_fkey FOREIGN KEY (user_id) REFERENCES users(user_id);


--
-- Name: public; Type: ACL; Schema: -; Owner: postgres
--

REVOKE ALL ON SCHEMA public FROM PUBLIC;
REVOKE ALL ON SCHEMA public FROM postgres;
GRANT ALL ON SCHEMA public TO postgres;
GRANT ALL ON SCHEMA public TO PUBLIC;


--
-- PostgreSQL database dump complete
--

