def return_verbose_level(config, logger):
    """
    Get the verbose level from the config file and return it.

    Parameters
    ----------
    config : dictionnary
        dictionnary containing the key values pair from the config file
    logger : logging object
        the logger used to print logs

    Returns
    -------
    logs : boolean
        if True, print the logs

    Examples
    --------
    >>> c = get_config({"--config" : "fink_grb/conf/fink_grb.conf"})
    >>> logger = init_logging()

    >>> return_verbose_level(c, logger)
    False
    """
    try:
        logs = config["ADMIN"]["verbose"] == "True"
    except Exception as e:
        logger.error(
            "Config entry not found \n\t {}\n\tsetting verbose to True by default".format(
                e
            )
        )
        logs = True

    return logs


if __name__ == "__main__":  # pragma: no cover
    import sys
    import doctest
    from pandas.testing import assert_frame_equal  # noqa: F401
    import pandas as pd  # noqa: F401
    import shutil  # noqa: F401
    from fink_grb.init import get_config, init_logging  # noqa: F401

    if "unittest.util" in __import__("sys").modules:
        # Show full diff in self.assertEqual.
        __import__("sys").modules["unittest.util"]._MAX_LENGTH = 999999999

    sys.exit(doctest.testmod()[0])
