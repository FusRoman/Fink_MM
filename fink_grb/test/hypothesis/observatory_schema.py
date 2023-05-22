from pandera import DataFrameSchema, Column, Check, Index


voevent_df_schema = DataFrameSchema(
    columns={
        "observatory": Column(
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
        "instrument": Column(
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
        "event": Column(
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
        "ivorn": Column(
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
        "triggerId": Column(
            dtype="str",
            checks=None,
            nullable=False,
            unique=True,
            coerce=False,
            required=True,
            regex=False,
            description=None,
            title=None,
        ),
        "ra": Column(
            dtype="float64",
            checks=[
                Check.greater_than_or_equal_to(min_value=0),
                Check.less_than_or_equal_to(max_value=360),
            ],
            nullable=False,
            unique=False,
            coerce=False,
            required=True,
            regex=False,
            description=None,
            title=None,
        ),
        "dec": Column(
            dtype="float64",
            checks=[
                Check.greater_than_or_equal_to(min_value=-90),
                Check.less_than_or_equal_to(max_value=90),
            ],
            nullable=False,
            unique=False,
            coerce=False,
            required=True,
            regex=False,
            description=None,
            title=None,
        ),
        "err_arcmin": Column(
            dtype="float64",
            checks=[Check.greater_than_or_equal_to(0)],
            nullable=False,
            unique=False,
            coerce=False,
            required=True,
            regex=False,
            description=None,
            title=None,
        ),
        "triggerTimejd": Column(
            dtype="float64",
            checks=[Check.greater_than_or_equal_to(min_value=0)],
            nullable=False,
            unique=False,
            coerce=False,
            required=True,
            regex=False,
            description=None,
            title=None,
        ),
        "triggerTimeUTC": Column(
            dtype="datetime64[ns, UTC]",
            checks=None,
            nullable=False,
            unique=False,
            coerce=False,
            required=True,
            regex=False,
            description=None,
            title=None,
        ),
        "raw_event": Column(
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
