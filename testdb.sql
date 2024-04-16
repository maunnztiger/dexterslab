PGDMP  5                    |           testdb    16.1    16.1 0    �           0    0    ENCODING    ENCODING     !   SET client_encoding = 'WIN1252';
                      false            �           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false            �           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false            �           1262    16401    testdb    DATABASE     z   CREATE DATABASE testdb WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE_PROVIDER = libc LOCALE = 'German_Germany.1252';
    DROP DATABASE testdb;
                postgres    false            �           0    0    DATABASE testdb    ACL     *   GRANT ALL ON DATABASE testdb TO testuser;
                   postgres    false    4837            �           0    0    testdb    DATABASE PROPERTIES     8   ALTER DATABASE testdb SET client_encoding TO 'win1252';
                     postgres    false            �            1259    16446    data_advantages    TABLE     �   CREATE TABLE public.data_advantages (
    id integer NOT NULL,
    aspect character varying(100) NOT NULL,
    value character varying(50) NOT NULL
);
 #   DROP TABLE public.data_advantages;
       public         heap    postgres    false            �            1259    16445 !   data_advantages_advantages_id_seq    SEQUENCE     �   CREATE SEQUENCE public.data_advantages_advantages_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 8   DROP SEQUENCE public.data_advantages_advantages_id_seq;
       public          postgres    false    224            �           0    0 !   data_advantages_advantages_id_seq    SEQUENCE OWNED BY     \   ALTER SEQUENCE public.data_advantages_advantages_id_seq OWNED BY public.data_advantages.id;
          public          postgres    false    223            �            1259    16453    data_disadvantages    TABLE     �   CREATE TABLE public.data_disadvantages (
    id integer NOT NULL,
    aspect character varying(100) NOT NULL,
    value character varying(50) NOT NULL
);
 &   DROP TABLE public.data_disadvantages;
       public         heap    postgres    false            �            1259    16452 '   data_disadvantages_disadvantages_id_seq    SEQUENCE     �   CREATE SEQUENCE public.data_disadvantages_disadvantages_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 >   DROP SEQUENCE public.data_disadvantages_disadvantages_id_seq;
       public          postgres    false    226            �           0    0 '   data_disadvantages_disadvantages_id_seq    SEQUENCE OWNED BY     e   ALTER SEQUENCE public.data_disadvantages_disadvantages_id_seq OWNED BY public.data_disadvantages.id;
          public          postgres    false    225            �            1259    16439    data_european_comparation    TABLE     �   CREATE TABLE public.data_european_comparation (
    id integer NOT NULL,
    aspect character varying(100) NOT NULL,
    value character varying(50) NOT NULL
);
 -   DROP TABLE public.data_european_comparation;
       public         heap    postgres    false            �            1259    16438 5   data_european_comparation_european_comparation_id_seq    SEQUENCE     �   CREATE SEQUENCE public.data_european_comparation_european_comparation_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 L   DROP SEQUENCE public.data_european_comparation_european_comparation_id_seq;
       public          postgres    false    222            �           0    0 5   data_european_comparation_european_comparation_id_seq    SEQUENCE OWNED BY     z   ALTER SEQUENCE public.data_european_comparation_european_comparation_id_seq OWNED BY public.data_european_comparation.id;
          public          postgres    false    221            �            1259    16404    data_general    TABLE     �   CREATE TABLE public.data_general (
    id integer NOT NULL,
    aspect character varying(100) NOT NULL,
    value character varying(50) NOT NULL
);
     DROP TABLE public.data_general;
       public         heap    postgres    false            �            1259    16403    data_general_general_id_seq    SEQUENCE     �   CREATE SEQUENCE public.data_general_general_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 2   DROP SEQUENCE public.data_general_general_id_seq;
       public          postgres    false    216            �           0    0    data_general_general_id_seq    SEQUENCE OWNED BY     S   ALTER SEQUENCE public.data_general_general_id_seq OWNED BY public.data_general.id;
          public          postgres    false    215            �            1259    16432    data_men    TABLE     �   CREATE TABLE public.data_men (
    id integer NOT NULL,
    aspect character varying(100) NOT NULL,
    value character varying(50) NOT NULL
);
    DROP TABLE public.data_men;
       public         heap    postgres    false            �            1259    16431    data_men_men_id_seq    SEQUENCE     �   CREATE SEQUENCE public.data_men_men_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 *   DROP SEQUENCE public.data_men_men_id_seq;
       public          postgres    false    220            �           0    0    data_men_men_id_seq    SEQUENCE OWNED BY     G   ALTER SEQUENCE public.data_men_men_id_seq OWNED BY public.data_men.id;
          public          postgres    false    219            �            1259    16425    data_special    TABLE     �   CREATE TABLE public.data_special (
    id integer NOT NULL,
    aspect character varying(100) NOT NULL,
    value character varying(50) NOT NULL
);
     DROP TABLE public.data_special;
       public         heap    postgres    false            �            1259    16424    data_special_special_id_seq    SEQUENCE     �   CREATE SEQUENCE public.data_special_special_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 2   DROP SEQUENCE public.data_special_special_id_seq;
       public          postgres    false    218            �           0    0    data_special_special_id_seq    SEQUENCE OWNED BY     S   ALTER SEQUENCE public.data_special_special_id_seq OWNED BY public.data_special.id;
          public          postgres    false    217            7           2604    16449    data_advantages id    DEFAULT     �   ALTER TABLE ONLY public.data_advantages ALTER COLUMN id SET DEFAULT nextval('public.data_advantages_advantages_id_seq'::regclass);
 A   ALTER TABLE public.data_advantages ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    224    223    224            8           2604    16456    data_disadvantages id    DEFAULT     �   ALTER TABLE ONLY public.data_disadvantages ALTER COLUMN id SET DEFAULT nextval('public.data_disadvantages_disadvantages_id_seq'::regclass);
 D   ALTER TABLE public.data_disadvantages ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    225    226    226            6           2604    16442    data_european_comparation id    DEFAULT     �   ALTER TABLE ONLY public.data_european_comparation ALTER COLUMN id SET DEFAULT nextval('public.data_european_comparation_european_comparation_id_seq'::regclass);
 K   ALTER TABLE public.data_european_comparation ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    222    221    222            3           2604    16407    data_general id    DEFAULT     z   ALTER TABLE ONLY public.data_general ALTER COLUMN id SET DEFAULT nextval('public.data_general_general_id_seq'::regclass);
 >   ALTER TABLE public.data_general ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    215    216    216            5           2604    16435    data_men id    DEFAULT     n   ALTER TABLE ONLY public.data_men ALTER COLUMN id SET DEFAULT nextval('public.data_men_men_id_seq'::regclass);
 :   ALTER TABLE public.data_men ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    220    219    220            4           2604    16428    data_special id    DEFAULT     z   ALTER TABLE ONLY public.data_special ALTER COLUMN id SET DEFAULT nextval('public.data_special_special_id_seq'::regclass);
 >   ALTER TABLE public.data_special ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    217    218    218            �          0    16446    data_advantages 
   TABLE DATA           <   COPY public.data_advantages (id, aspect, value) FROM stdin;
    public          postgres    false    224   S6       �          0    16453    data_disadvantages 
   TABLE DATA           ?   COPY public.data_disadvantages (id, aspect, value) FROM stdin;
    public          postgres    false    226   7       �          0    16439    data_european_comparation 
   TABLE DATA           F   COPY public.data_european_comparation (id, aspect, value) FROM stdin;
    public          postgres    false    222   �7       �          0    16404    data_general 
   TABLE DATA           9   COPY public.data_general (id, aspect, value) FROM stdin;
    public          postgres    false    216   g8       �          0    16432    data_men 
   TABLE DATA           5   COPY public.data_men (id, aspect, value) FROM stdin;
    public          postgres    false    220   �9       �          0    16425    data_special 
   TABLE DATA           9   COPY public.data_special (id, aspect, value) FROM stdin;
    public          postgres    false    218   g:       �           0    0 !   data_advantages_advantages_id_seq    SEQUENCE SET     P   SELECT pg_catalog.setval('public.data_advantages_advantages_id_seq', 1, false);
          public          postgres    false    223            �           0    0 '   data_disadvantages_disadvantages_id_seq    SEQUENCE SET     V   SELECT pg_catalog.setval('public.data_disadvantages_disadvantages_id_seq', 1, false);
          public          postgres    false    225            �           0    0 5   data_european_comparation_european_comparation_id_seq    SEQUENCE SET     d   SELECT pg_catalog.setval('public.data_european_comparation_european_comparation_id_seq', 1, false);
          public          postgres    false    221            �           0    0    data_general_general_id_seq    SEQUENCE SET     J   SELECT pg_catalog.setval('public.data_general_general_id_seq', 13, true);
          public          postgres    false    215            �           0    0    data_men_men_id_seq    SEQUENCE SET     B   SELECT pg_catalog.setval('public.data_men_men_id_seq', 1, false);
          public          postgres    false    219            �           0    0    data_special_special_id_seq    SEQUENCE SET     J   SELECT pg_catalog.setval('public.data_special_special_id_seq', 1, false);
          public          postgres    false    217            B           2606    16451 $   data_advantages data_advantages_pkey 
   CONSTRAINT     b   ALTER TABLE ONLY public.data_advantages
    ADD CONSTRAINT data_advantages_pkey PRIMARY KEY (id);
 N   ALTER TABLE ONLY public.data_advantages DROP CONSTRAINT data_advantages_pkey;
       public            postgres    false    224            D           2606    16458 *   data_disadvantages data_disadvantages_pkey 
   CONSTRAINT     h   ALTER TABLE ONLY public.data_disadvantages
    ADD CONSTRAINT data_disadvantages_pkey PRIMARY KEY (id);
 T   ALTER TABLE ONLY public.data_disadvantages DROP CONSTRAINT data_disadvantages_pkey;
       public            postgres    false    226            @           2606    16444 8   data_european_comparation data_european_comparation_pkey 
   CONSTRAINT     v   ALTER TABLE ONLY public.data_european_comparation
    ADD CONSTRAINT data_european_comparation_pkey PRIMARY KEY (id);
 b   ALTER TABLE ONLY public.data_european_comparation DROP CONSTRAINT data_european_comparation_pkey;
       public            postgres    false    222            :           2606    16409    data_general data_general_pkey 
   CONSTRAINT     \   ALTER TABLE ONLY public.data_general
    ADD CONSTRAINT data_general_pkey PRIMARY KEY (id);
 H   ALTER TABLE ONLY public.data_general DROP CONSTRAINT data_general_pkey;
       public            postgres    false    216            >           2606    16437    data_men data_men_pkey 
   CONSTRAINT     T   ALTER TABLE ONLY public.data_men
    ADD CONSTRAINT data_men_pkey PRIMARY KEY (id);
 @   ALTER TABLE ONLY public.data_men DROP CONSTRAINT data_men_pkey;
       public            postgres    false    220            <           2606    16430    data_special data_special_pkey 
   CONSTRAINT     \   ALTER TABLE ONLY public.data_special
    ADD CONSTRAINT data_special_pkey PRIMARY KEY (id);
 H   ALTER TABLE ONLY public.data_special DROP CONSTRAINT data_special_pkey;
       public            postgres    false    218            �   �   x�E���0���S��ը��
����q)�(� -��gw�$�������Ý�liu�hRxvx#�j��P�*4��+Y�P*)PS��97:���ed�)����yGPR�� �T�y��'���R0�Ѥ~v�&��S�#1j�X��*�NP�%�n���=y� �c'�� �H�      �   �   x�=��
1E��+��V�]K��B��f'�N`LV�{���vw��9w.��R��HI��r�!�E릒�ΌD�,���E�2�pb?��+D���R�����K�N�$�r�>A�Y;0ߟ��zS�Z����9���*lt�rU&����x��.��LJ��@DV      �   �   x�%�A�0D����]c(�U�����ʭ��?@
��xRO�A]�dޛ�en�х;� ��xr�CiA9J���T�=/yh{�L��)�����V�A*+W�����FkYڣ^ܸ�b�qy�nj#sM�Ӌ�&�f����}I+�      �   L  x�]�1O�0���W��U�Ȏ�@U�X���ϒ�4?��g�e`;�������x1�cO`�o!�S�;�܂�|��b�X��[�ɒ�Dz���H|�ёa�زsdl��QT�Y�*֧@;/_�6Pw�g�!�#B���i�N�A���ԙ~�+�Ʊ��+:�,=�>��!�}��aT/�LVG/԰&���L��#��0\��
�O95�sa4��;W5�S.m�O��8����C&����Ab]�^�Tr�n~�>�>@�bQU��*ڇ��6���ȷFؽnDg��ӘnI���rQ��oLi����l:�v}\�e���j      �   �   x�u�;�0Dk�)�q�B�E)(�����? ��#Bt����4j�S!�%;�g�	�}GBbO8JpXtb�Vrq"U�jh�pz�Gv���`�>=���T�bԪ��}�X�p�n!�k���%���U�z���3 xCe?�      �   �   x�M��j�@E뙯�f�,��t%C ��iV�l����J���7���r��a�r��4p(=�ʉ��c���R؋f1�>@�7���\��V�#g���d�,-�eI\.����c�'�q�q�#'M�tGU��\�fkp���u�S~��>�r��1�`�6���e�H8�Rɦo��+_G?/s�����0��emp�0��mN�Ͷ\qж�^��eY     