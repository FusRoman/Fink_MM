from pandera import DataFrameSchema, Column, Check, Index

# minimum set of column required by fink_grb for candidate field in the ztf alerts
fink_candidate_schema = DataFrameSchema(
    columns={
        "ssdistnr": Column(
            dtype="float64",
            checks=[
                Check.greater_than_or_equal_to(0),
                Check.less_than_or_equal_to(30)
            ],
            nullable=False,
            unique=False,
            coerce=False,
            required=True,
            regex=False,
            description="distance to nearest known solar system object; set to -999.0 if none [arcsec]",
            title=None,
        ),
        "distpsnr1": Column(
            dtype="float64",
            checks=[
                Check.greater_than_or_equal_to(0),
                Check.less_than_or_equal_to(30)
            ],
            nullable=False,
            unique=False,
            coerce=False,
            required=True,
            regex=False,
            description="Distance of closest source from PS1 catalog; if exists within 30 arcsec [arcsec]",
            title=None,
        ),
        "neargaia": Column(
            dtype="float64",
            checks=[
                Check.greater_than_or_equal_to(0),
                Check.less_than_or_equal_to(90)
            ],
            nullable=False,
            unique=False,
            coerce=False,
            required=True,
            regex=False,
            description="Distance to closest source from Gaia DR1 catalog irrespective of magnitude; if exists within 90 arcsec [arcsec]",
            title=None,
        ),
        "ra": Column(
            dtype="float64",
            checks=[
                Check.greater_than_or_equal_to(0),
                Check.less_than_or_equal_to(360),
            ],
            nullable=False,
            unique=False,
            coerce=False,
            required=True,
            regex=False,
            description="Right Ascension of candidate; J2000 [deg]",
            title=None,
        ),
        "dec": Column(
            dtype="float64",
            checks=[
                Check.greater_than_or_equal_to(-90),
                Check.less_than_or_equal_to(90),
            ],
            nullable=False,
            unique=False,
            coerce=False,
            required=True,
            regex=False,
            description="Declination of candidate; J2000 [deg]",
            title=None,
        ),
        "jdstarthist": Column(
            dtype="float64",
            checks=[
                Check.greater_than_or_equal_to(0)
            ],
            nullable=False,
            unique=False,
            coerce=False,
            required=True,
            regex=False,
            description="Earliest Julian date of epoch corresponding to ndethist [days]",
            title=None,
        ),
        "ndethist": Column(
            dtype="int64",
            checks=[
                Check.greater_than_or_equal_to(0)
            ],
            nullable=False,
            unique=False,
            coerce=False,
            required=True,
            regex=False,
            description="Number of spatially-coincident detections falling within 1.5 arcsec going back to beginning of survey; only detections that fell on the same field and readout-channel ID where the input candidate was observed are counted. All raw detections down to a photometric S/N of ~ 3 are included.",
            title=None,
        ),
        "drb": Column(
            dtype="float64",
            checks=[
                Check.greater_than_or_equal_to(0),
                Check.less_than_or_equal_to(1)
            ],
            nullable=False,
            unique=False,
            coerce=False,
            required=True,
            regex=False,
            description="RealBogus quality score from Deep-Learning-based classifier; range is 0 to 1 where closer to 1 is more reliable",
            title=None,
        ),
        "classtar": Column(
            dtype="float64",
            checks=[
                Check.greater_than_or_equal_to(0),
                Check.less_than_or_equal_to(1)
            ],
            nullable=False,
            unique=False,
            coerce=False,
            required=True,
            regex=False,
            description="Star/Galaxy classification score from SExtractor",
            title=None,
        ),
    },
    checks=None,
    index=Index(
        dtype="int64",
        checks=[Check.greater_than_or_equal_to(0)],
        nullable=False,
        coerce=False,
        name=None,
        description=None,
        title=None,
    ),
    dtype=None,
    coerce=True,
    strict=False,
    name=None,
    ordered=False,
    unique=None,
    report_duplicates="all",
    unique_column_names=False,
    title=None,
    description=None,
)

magpsf_col = Column(
    dtype="float64",
    checks=[Check.greater_than_or_equal_to(8), Check.less_than_or_equal_to(23)],
    nullable=False,
    unique=False,
    coerce=False,
    required=True,
    regex=False,
    description="magnitude from PSF-fit photometry [mag]",
    title="magpsf",
)

diffmaglim = Column(
    dtype="float64",
    checks=[Check.greater_than_or_equal_to(8), Check.less_than_or_equal_to(23)],
    nullable=False,
    unique=False,
    coerce=False,
    required=True,
    regex=False,
    description="5-sigma mag limit in difference image based on PSF-fit photometry [mag]",
    title="diffmaglim",
)

jd = Column(
    dtype="float64",
    checks=[Check.greater_than(0)],
    nullable=False,
    unique=False,
    coerce=False,
    required=True,
    regex=False,
    description="Observation Julian date at start of exposure [days]",
    title="jd",
)

fid = Column(
    dtype="int64",
    checks=[Check.isin([1, 2, 3])],
    nullable=False,
    unique=False,
    coerce=False,
    required=True,
    regex=False,
    description="Filter ID (1=g; 2=r; 3=i)",
    title="fid",
)


fink_alert_minimal_schema = DataFrameSchema(
    columns={
        "objectId": Column(
            dtype="str",
            checks=[Check.str_matches("ZTF[0-9]{2}[a-z]{7}")],
            nullable=False,
            unique=False,
            coerce=False,
            required=True,
            regex=False,
            description="unique identifier for this object",
            title=None,
        ),
        "candid": Column(
            dtype="int64",
            checks=[Check.greater_than(0)],
            nullable=False,
            unique=True,
            coerce=False,
            required=True,
            regex=False,
            description="unique identifier for the subtraction candidate",
            title=None,
        ),
        "cdsxmatch": Column(
            dtype="str",
            checks=None,
            nullable=False,
            unique=False,
            coerce=False,
            required=True,
            regex=False,
            description=None,
            title=None,
        ),
        "roid": Column(
            dtype="int32",
            checks=[
                Check.greater_than_or_equal_to(min_value=0.0),
                Check.less_than_or_equal_to(max_value=3.0),
            ],
            nullable=False,
            unique=False,
            coerce=False,
            required=True,
            regex=False,
            description=None,
            title=None,
        ),
        "rf_snia_vs_nonia": Column(
            dtype="float64",
            checks=[
                Check.greater_than_or_equal_to(min_value=0.0),
                Check.less_than_or_equal_to(max_value=1.0),
            ],
            nullable=False,
            unique=False,
            coerce=False,
            required=True,
            regex=False,
            description=None,
            title=None,
        ),
        "snn_snia_vs_nonia": Column(
            dtype="float64",
            checks=[
                Check.greater_than_or_equal_to(min_value=0.0),
                Check.less_than_or_equal_to(max_value=1.0),
            ],
            nullable=False,
            unique=False,
            coerce=False,
            required=True,
            regex=False,
            description=None,
            title=None,
        ),
        "snn_sn_vs_all": Column(
            dtype="float64",
            checks=[
                Check.greater_than_or_equal_to(min_value=0.0),
                Check.less_than_or_equal_to(max_value=1.0),
            ],
            nullable=False,
            unique=False,
            coerce=False,
            required=True,
            regex=False,
            description=None,
            title=None,
        ),
        "mulens": Column(
            dtype="float64",
            checks=[
                Check.greater_than_or_equal_to(min_value=0.0),
                Check.less_than_or_equal_to(max_value=1.0),
            ],
            nullable=False,
            unique=False,
            coerce=False,
            required=True,
            regex=False,
            description=None,
            title=None,
        ),
        "rf_kn_vs_nonkn": Column(
            dtype="float64",
            checks=[
                Check.greater_than_or_equal_to(min_value=0.0),
                Check.less_than_or_equal_to(max_value=1.0),
            ],
            nullable=False,
            unique=False,
            coerce=False,
            required=True,
            regex=False,
            description=None,
            title=None,
        ),
        "tracklet": Column(
            dtype="str",
            checks=None,
            nullable=True,
            unique=False,
            coerce=False,
            required=True,
            regex=False,
            description=None,
            title=None,
        ),
    },
    checks=None,
    index=Index(
        dtype="int64",
        checks=[Check.greater_than_or_equal_to(0)],
        nullable=False,
        coerce=False,
        name=None,
        description=None,
        title=None,
    ),
    dtype=None,
    coerce=True,
    strict=False,
    name=None,
    ordered=False,
    unique=None,
    report_duplicates="all",
    unique_column_names=False,
    title=None,
    description=None,
)
