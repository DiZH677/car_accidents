DROP TABLE IF EXISTS DTP CASCADE;
CREATE TABLE DTP
(
    id serial primary key,
    description varchar(100),
    datetime timestamp,
    coord_w float,
    coord_l float,
    dor varchar(200),
    osv varchar(50),
    count_ts int,
    count_parts int
);

DROP TABLE IF EXISTS VEHICLE CASCADE;
CREATE TABLE VEHICLE
(
    id serial primary key,
    dtp_id int,
    marka_ts varchar(100),
    m_ts varchar(100),
    r_rul varchar(50),
    type_ts varchar(200),
    car_year int,
    color varchar(15),
    FOREIGN KEY(dtp_id) REFERENCES DTP(id)
);

DROP TABLE IF EXISTS PARTICIPANT CASCADE;
CREATE TABLE PARTICIPANT
(
    id serial primary key,
    vehicle_id int,
    category varchar(50),
    warnings varchar(400),
    SAFETY_BELT bool,
    pol varchar(15),
    health varchar(200),
    FOREIGN KEY (vehicle_id) REFERENCES VEHICLE(id)
);
