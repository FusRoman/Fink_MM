# Fink_GRB
Correlation of the Fink alerts with multi-messenger instruments
* Available Instrument
    * Gamma-Ray: Fermi, Swift, Integral
    * X-Ray: Swift
    * Optical: Swift
    * Neutrino: IceCube

## Installation Procedure

* Clone the repository
```console
toto@linux:~$ git clone https://github.com/FusRoman/Fink_GRB.git
```
* Install with pip
```console
toto@linux:~$ pip install .
```
* Copy the default config file in a custom location
```console
toto@linux:~$ cp fink_grb/conf/fink_grb.conf /config_path
```
and update your configuration file with your custom parameters.
Please note, the paths in the configuration file must not end with a '/'.

### Setup the Fink_GRB daemons
* Start listening to GCN
```console
toto@linux:~$ fink_grb gcn_stream start --config /config_path 
```
The above command will start a daemon that will store the GCN issued from the instruments registered in the system. The GNC will be stored at the location specified in the configuration file by the entry named 'online_gcn_data_prefix'. The path can be a local path or a hdfs path. In the latter case, the path must start with hdfs://IP:PORT///your_path where IP and PORT refer to the hdfs driver.

Fink_GRB has multiples script in the scheduler folder to launch the different services.
* science2grb.sh will launch the online services that will cross-match in real-time the alerts issued from the ZTF/LSST with incoming GCN. (latency: ZTF/LSST latency + 30 seconds max)
* science2grb_offline.sh launch the offline services that will cross-match all the latest alerts from ZTF/LSST with the GCN within the time window (in days) specified in your config file. (latency: 1 day)
* grb2distribution.sh launch the distribution services that will send the outputs of the online services in real-time to the registered users of the [fink-client](https://github.com/astrolabsoftware/fink-client). (latency: ZTF/LSST latency + 30 seconds + Network latency to reach fink-client)

The three scripts are not meant to be launched lonely but with cron jobs. The following lines have to be put in the cron file.
```
0 01 * * * /custom_install_path/scheduler/science2grb.sh
0 01 * * * /custom_install_path/scheduler/grb2distribution.sh
1 17 * * * /custom_install_path/scheduler/science2grb_offline.sh
```
The above lines will launch the streaming services daily at 01:00 AM (Paris Timezone) until the end date specified in the scheduler script file. For both science2grb.sh and grb2distribution.sh, they finished at 05:00 PM (Paris Timezone). The start and end times have been set for ZTF (01:00 AM Paris -> 4:00 PM California / 5:00 PM Paris -> 08:00 AM California) and must be modified for LSST.
The offline services start at 5:01 PM daily and finish automatically at the end of the process. 