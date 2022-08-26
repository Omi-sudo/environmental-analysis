SELECT
  loc_name,
  instit_id,
  sed_code,
  legal_name,
  popular_name,
  label_name,
  CAST(county_code AS STRING) AS country_code,
  county_desc,
  established_date,
  active_date,
  inst_typ_cd,
  inst_type_desc,
  instsubtypcod,
  instsubtypdesc,
  ins_parent_id,
  insparentidnm,
  record_type_code,
  record_type_desc,
  comm_type_code,
  community_type_desc,
  dist_type_code,
  dist_type_desc,
  sdl_code,
  sdl_desc,
  muni_code,
  rcc_code,
  ric_code,
  geographic_region_code,
  physaddrline2,
  physzipadd4,
  phys_addr_mod_date,
  ceo_fname,
  ceo_mi,
  ceo_lname,
  ceo_title,
  ceo_salute,
  ceo_phonenum,
  ceo_phoneext,
  ceo_email,
  insiturl,
  grade_pk,
  grade_hk,
  grade_fk,
  grade_1,
  grade_2,
  grade_3,
  grade_4,
  grade_5,
  grade_6,
  grade_uge,
  grade_7,
  grade_8,
  grade_9,
  grade_10,
  grade_11,
  grade_12,
  grade_ugs,
  grade_org_code,
  grade_organization_desc,
  ftp_update,
  latitude,
  longitude,
  ST_GeogPoint(longitude, latitude) AS geometry,
  acc_code,
  updatedby,
  date_,
  gpo_notes,
  physaddr_1,
  physcity,
  physicalstate,
  physzipcd5,
  boces_code,
  locator_defintion,
  record_date,
  ingestion_timestamp
FROM
  `ingestion.nys_public_school_k_12`