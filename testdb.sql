PGDMP      8                |           testdb    16.1    16.1 3    �           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false            �           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false            �           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false            �           1262    16401    testdb    DATABASE     z   CREATE DATABASE testdb WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE_PROVIDER = libc LOCALE = 'German_Germany.1252';
    DROP DATABASE testdb;
                postgres    false            �           0    0    DATABASE testdb    ACL     *   GRANT ALL ON DATABASE testdb TO testuser;
                   postgres    false    4844            �           0    0    testdb    DATABASE PROPERTIES     8   ALTER DATABASE testdb SET client_encoding TO 'win1252';
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
          public          postgres    false    217            �            1259    24685    video_source    TABLE     p   CREATE TABLE public.video_source (
    id integer NOT NULL,
    video_source character varying(100) NOT NULL
);
     DROP TABLE public.video_source;
       public         heap    postgres    false            ;           2604    16449    data_advantages id    DEFAULT     �   ALTER TABLE ONLY public.data_advantages ALTER COLUMN id SET DEFAULT nextval('public.data_advantages_advantages_id_seq'::regclass);
 A   ALTER TABLE public.data_advantages ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    223    224    224            <           2604    16456    data_disadvantages id    DEFAULT     �   ALTER TABLE ONLY public.data_disadvantages ALTER COLUMN id SET DEFAULT nextval('public.data_disadvantages_disadvantages_id_seq'::regclass);
 D   ALTER TABLE public.data_disadvantages ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    226    225    226            :           2604    16442    data_european_comparation id    DEFAULT     �   ALTER TABLE ONLY public.data_european_comparation ALTER COLUMN id SET DEFAULT nextval('public.data_european_comparation_european_comparation_id_seq'::regclass);
 K   ALTER TABLE public.data_european_comparation ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    221    222    222            7           2604    16407    data_general id    DEFAULT     z   ALTER TABLE ONLY public.data_general ALTER COLUMN id SET DEFAULT nextval('public.data_general_general_id_seq'::regclass);
 >   ALTER TABLE public.data_general ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    215    216    216            9           2604    16435    data_men id    DEFAULT     n   ALTER TABLE ONLY public.data_men ALTER COLUMN id SET DEFAULT nextval('public.data_men_men_id_seq'::regclass);
 :   ALTER TABLE public.data_men ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    220    219    220            8           2604    16428    data_special id    DEFAULT     z   ALTER TABLE ONLY public.data_special ALTER COLUMN id SET DEFAULT nextval('public.data_special_special_id_seq'::regclass);
 >   ALTER TABLE public.data_special ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    217    218    218            �          0    16446    data_advantages 
   TABLE DATA           <   COPY public.data_advantages (id, aspect, value) FROM stdin;
    public          postgres    false    224   {9       �          0    16453    data_disadvantages 
   TABLE DATA           ?   COPY public.data_disadvantages (id, aspect, value) FROM stdin;
    public          postgres    false    226   8:       �          0    16439    data_european_comparation 
   TABLE DATA           F   COPY public.data_european_comparation (id, aspect, value) FROM stdin;
    public          postgres    false    222   �:       �          0    16404    data_general 
   TABLE DATA           9   COPY public.data_general (id, aspect, value) FROM stdin;
    public          postgres    false    216   �;       �          0    16432    data_men 
   TABLE DATA           5   COPY public.data_men (id, aspect, value) FROM stdin;
    public          postgres    false    220   #=       �          0    16425    data_special 
   TABLE DATA           9   COPY public.data_special (id, aspect, value) FROM stdin;
    public          postgres    false    218   �=       �          0    24685    video_source 
   TABLE DATA           8   COPY public.video_source (id, video_source) FROM stdin;
    public          postgres    false    227   �>       �           0    0 !   data_advantages_advantages_id_seq    SEQUENCE SET     P   SELECT pg_catalog.setval('public.data_advantages_advantages_id_seq', 1, false);
          public          postgres    false    223            �           0    0 '   data_disadvantages_disadvantages_id_seq    SEQUENCE SET     V   SELECT pg_catalog.setval('public.data_disadvantages_disadvantages_id_seq', 1, false);
          public          postgres    false    225            �           0    0 5   data_european_comparation_european_comparation_id_seq    SEQUENCE SET     d   SELECT pg_catalog.setval('public.data_european_comparation_european_comparation_id_seq', 1, false);
          public          postgres    false    221            �           0    0    data_general_general_id_seq    SEQUENCE SET     J   SELECT pg_catalog.setval('public.data_general_general_id_seq', 13, true);
          public          postgres    false    215            �           0    0    data_men_men_id_seq    SEQUENCE SET     B   SELECT pg_catalog.setval('public.data_men_men_id_seq', 1, false);
          public          postgres    false    219            �           0    0    data_special_special_id_seq    SEQUENCE SET     J   SELECT pg_catalog.setval('public.data_special_special_id_seq', 1, false);
          public          postgres    false    217            F           2606    16451 $   data_advantages data_advantages_pkey 
   CONSTRAINT     b   ALTER TABLE ONLY public.data_advantages
    ADD CONSTRAINT data_advantages_pkey PRIMARY KEY (id);
 N   ALTER TABLE ONLY public.data_advantages DROP CONSTRAINT data_advantages_pkey;
       public            postgres    false    224            H           2606    16458 *   data_disadvantages data_disadvantages_pkey 
   CONSTRAINT     h   ALTER TABLE ONLY public.data_disadvantages
    ADD CONSTRAINT data_disadvantages_pkey PRIMARY KEY (id);
 T   ALTER TABLE ONLY public.data_disadvantages DROP CONSTRAINT data_disadvantages_pkey;
       public            postgres    false    226            D           2606    16444 8   data_european_comparation data_european_comparation_pkey 
   CONSTRAINT     v   ALTER TABLE ONLY public.data_european_comparation
    ADD CONSTRAINT data_european_comparation_pkey PRIMARY KEY (id);
 b   ALTER TABLE ONLY public.data_european_comparation DROP CONSTRAINT data_european_comparation_pkey;
       public            postgres    false    222            >           2606    16409    data_general data_general_pkey 
   CONSTRAINT     \   ALTER TABLE ONLY public.data_general
    ADD CONSTRAINT data_general_pkey PRIMARY KEY (id);
 H   ALTER TABLE ONLY public.data_general DROP CONSTRAINT data_general_pkey;
       public            postgres    false    216            B           2606    16437    data_men data_men_pkey 
   CONSTRAINT     T   ALTER TABLE ONLY public.data_men
    ADD CONSTRAINT data_men_pkey PRIMARY KEY (id);
 @   ALTER TABLE ONLY public.data_men DROP CONSTRAINT data_men_pkey;
       public            postgres    false    220            @           2606    16430    data_special data_special_pkey 
   CONSTRAINT     \   ALTER TABLE ONLY public.data_special
    ADD CONSTRAINT data_special_pkey PRIMARY KEY (id);
 H   ALTER TABLE ONLY public.data_special DROP CONSTRAINT data_special_pkey;
       public            postgres    false    218            J           2606    24689    video_source video_source_pkey 
   CONSTRAINT     \   ALTER TABLE ONLY public.video_source
    ADD CONSTRAINT video_source_pkey PRIMARY KEY (id);
 H   ALTER TABLE ONLY public.video_source DROP CONSTRAINT video_source_pkey;
       public            postgres    false    227            �   �   x�E�A�0E��Ș[#b�[XxM��"Ci(i)$�͝�$���{�������^ɴ�9l(`��T��(�Ty�K
˵�}"p+�����`�%(r)�&�~�g��K�"P')r����~��&��S�1j�X�_~�|G(�S7�a����Iq�	!>�vIa      �   �   x�=�=
1����l+ꮈ��"�Xh#6�����<�7�bfA�����{S�C�:d8DJ���K-�X6���;pb$�da��l SG��J�B4�J���S��K���H��5��t���}J?��W��Ŗ��=�S.٪Eg*wPe����h��(��N���D�      �   �   x�%�A�0D����]c(�U�����ʭ��?@(�H<�'�&\L��L�IP�<�u�]��R(�O���JJ��o:PJP��=N��[�D��)���+� �2�dV�:��Ӆ�2�G99��l�qy�n��F��8�/�960��mGD_I,�      �   }  x�m�1n�0Ek�,V���ڊK��"� i����4E3��<9�v�X�r
!�n����R��8�Ѵ@�	��li����d��ܨ�jS����M���/H���Y����L��=p�䬪��^��'p����9���b��\z=W�#���´G�'��0
mz�x�EF����������B���ng� �xar��&j���v�[��1xy`~��R4'�V���,K}�v�RTu{��]�[����W���Bo�s�q�N����b
��a3L�񁒀���`&�r���12��U�{J���rs$�2�%߫z%�J=�?�b�o`;FN�r�q�[�*�@_�
W��0w���1��!$�1���Z:���^k�?e��6      �   �   x�u�=
�@F��SL���IPkED���&?ܝ���=�ǰ��,���x�B����!���>BD�#R���{ �+�bnB��{UdFgjW>=9�N��A�w���M���Wj�0:��^$�s�+�u�^�f�B�u���C&p�}�R����.�F�!����\k���Jf      �   �   x�M�=j�@��SL��	�lCR�r �@j7+i6Z؟��J�����.�e����񾯁�ұ���N��,�8�\��^4�����-|L���`��r���l��ŴL��%B�lp���z\t���IE�Yզ!��A����a�s�j������+��	�akp{��	�N*����s����|������#�W�뇤�H�S����5xxB�3�$ge      �      x������ � �     