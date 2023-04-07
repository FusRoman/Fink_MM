import pytest
import os
import pandas
import tempfile
from pandas.testing import assert_frame_equal

from fink_grb.gcn_stream.gcn_reader import load_voevent_from_path
from fink_grb.observatory import voevent_to_class


@pytest.fixture(autouse=True)
def init_test(doctest_namespace):
    doctest_namespace["pd"] = pandas
    doctest_namespace["tempfile"] = tempfile
    doctest_namespace["assert_frame_equal"] = assert_frame_equal
    doctest_namespace["load_voevent_from_path"] = load_voevent_from_path
    doctest_namespace["voevent_to_class"] = voevent_to_class


@pytest.fixture(autouse=True)
def init_fermi(doctest_namespace):

    doctest_namespace["fermi_gbm_voevent_path"] = 'fink_grb/test/test_data/VODB/fermi/voevent_number=193.xml'
    doctest_namespace["fermi_lat_voevent_path"] = 'fink_grb/test/test_data/VODB/fermi/voevent_number=2842.xml'

    fermi_gbm = voevent_to_class(load_voevent_from_path(doctest_namespace["fermi_gbm_voevent_path"]))
    fermi_lat = voevent_to_class(load_voevent_from_path(doctest_namespace["fermi_lat_voevent_path"]))

    
    doctest_namespace["fermi_gbm"] = fermi_gbm
    doctest_namespace["fermi_lat"] = fermi_lat

@pytest.fixture(autouse=True)
def init_swift(doctest_namespace):

    doctest_namespace["swift_bat_voevent_path"] = 'fink_grb/test/test_data/VODB/swift/voevent_number=392.xml'
    doctest_namespace["swift_xrt_voevent_path"] = 'fink_grb/test/test_data/VODB/swift/voevent_number=4554.xml'
    doctest_namespace["swift_uvot_voevent_path"] = 'fink_grb/test/test_data/VODB/swift/voevent_number=8582.xml'

    swift_bat = voevent_to_class(load_voevent_from_path(doctest_namespace["swift_bat_voevent_path"]))
    swift_xrt = voevent_to_class(load_voevent_from_path(doctest_namespace["swift_xrt_voevent_path"]))
    swift_uvot = voevent_to_class(load_voevent_from_path(doctest_namespace["swift_uvot_voevent_path"]))

    doctest_namespace["swift_bat"] = swift_bat
    doctest_namespace["swift_xrt"] = swift_xrt
    doctest_namespace["swift_uvot"] = swift_uvot

@pytest.fixture(autouse=True)
def init_integral(doctest_namespace):

    doctest_namespace["integral_weak_voevent_path"] = 'fink_grb/test/test_data/VODB/integral/voevent_number=737.xml'
    doctest_namespace["integral_wakeup_voevent_path"] = 'fink_grb/test/test_data/VODB/integral/voevent_number=18790.xml'
    doctest_namespace["integral_refined_voevent_path"] = 'fink_grb/test/test_data/VODB/integral/voevent_number=18791.xml'

    integral_weak = voevent_to_class(load_voevent_from_path(doctest_namespace["integral_weak_voevent_path"]))
    integral_wakeup = voevent_to_class(load_voevent_from_path(doctest_namespace["integral_wakeup_voevent_path"]))
    integral_refined = voevent_to_class(load_voevent_from_path(doctest_namespace["integral_refined_voevent_path"]))

    doctest_namespace["integral_weak"] = integral_weak
    doctest_namespace["integral_wakeup"] = integral_wakeup
    doctest_namespace["integral_refined"] = integral_refined

@pytest.fixture(autouse=True)
def init_icecube(doctest_namespace):

    doctest_namespace["icecube_cascade_voevent_path"] = 'fink_grb/test/test_data/VODB/icecube/voevent_number=825.xml'
    doctest_namespace["icecube_bronze_voevent_path"] = 'fink_grb/test/test_data/VODB/icecube/voevent_number=3028.xml'
    doctest_namespace["icecube_gold_voevent_path"] = 'fink_grb/test/test_data/VODB/icecube/voevent_number=45412.xml'

    icecube_cascade = voevent_to_class(load_voevent_from_path(doctest_namespace["icecube_cascade_voevent_path"]))
    icecube_bronze = voevent_to_class(load_voevent_from_path(doctest_namespace["icecube_bronze_voevent_path"]))
    icecube_gold = voevent_to_class(load_voevent_from_path(doctest_namespace["icecube_gold_voevent_path"]))

    doctest_namespace["icecube_cascade"] = icecube_cascade
    doctest_namespace["icecube_bronze"] = icecube_bronze
    doctest_namespace["icecube_gold"] = icecube_gold

@pytest.fixture(autouse=True, scope="session")
def init_spark(doctest_namespace):

    from astropy.time import Time
    import os

    doctest_namespace["Time"] = Time

    grb_data = "fink_grb/test/test_data/gcn_test/raw/year=2019/month=09/day=03"
    join_data = "fink_grb/test/test_data/join_raw_datatest.parquet"
    alert_data = "fink_grb/test/test_data/ztf_test/online/science/year=2019/month=09/day=03/"

    doctest_namespace["grb_data"] = grb_data
    doctest_namespace["join_data"] = join_data
    doctest_namespace["alert_data"] = alert_data


    ztf_datatest = "fink_grb/test/test_data/ztf_test/online"
    gcn_datatest = "fink_grb/test/test_data/gcn_test"
    join_data_test = "fink_grb/test/test_data/grb_join_output.parquet"

    doctest_namespace["ztf_datatest"] = ztf_datatest
    doctest_namespace["gcn_datatest"] = gcn_datatest
    doctest_namespace["join_data_test"] = join_data_test

    fink_home = os.environ["FINK_HOME"]
    hbase_catalog = fink_home + "/catalogs_hbase/ztf.jd.json"

    doctest_namespace["fink_home"] = fink_home
    doctest_namespace["hbase_catalog"] = hbase_catalog

    from fink_client.consumer import AlertConsumer
    import tabulate

    maxtimeout = 5
    myconfig = {"username": "rlm", "bootstrap.servers": "localhost:9092", "group_id": "rlm_fink"}
    topics = ["fink_grb_bronze"]

    headers = [
        "Generated at (jd)",
        "Topic",
        "objectId",
        "Fink_Class",
        "Rate",
    ]

    doctest_namespace["AlertConsumer"] = AlertConsumer
    doctest_namespace["tabulate"] = tabulate
    doctest_namespace["ztfxgcn_test"] = "fink_grb/test/test_data/ztfxgcn_test/"
    doctest_namespace["headers"] = headers
    doctest_namespace["maxtimeout"] = maxtimeout
    doctest_namespace["myconfig"] = myconfig
    doctest_namespace["topics"] = topics

    from pyspark.sql import SparkSession
    from pyspark import SparkConf

    conf = SparkConf()
    confdic = {
        "spark.jars.packages": os.environ["FINK_PACKAGES"],
        "spark.jars": os.environ["FINK_JARS"],
        # "spark.python.daemon.module": "coverage_daemon",
    }
    conf.setMaster("local[2]")
    conf.setAppName("fink_test")
    for k, v in confdic.items():
        conf.set(key=k, value=v)
    spark = SparkSession.builder.appName("fink_test").config(conf=conf).getOrCreate()

    # Reduce the number of suffled partitions
    spark.conf.set("spark.sql.shuffle.partitions", 2)

    doctest_namespace["spark"] = spark