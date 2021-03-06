# ber-visualizer




  <h3 align="center">BER Visualizer</h3>

  <p align="center">
    A graph-generator that can process large amounts of VLC data and return a graph comparing BERs (Bit Error Rates).
    <br />
  </p>
</p>

## Prerequisites

* pip
  ```sh
  pip install pandas
  pip install matplotlib
  ```

## Installation

1. Clone the repo
   ```sh
   git clone https://github.com/sam-shridhar1950f/ber-visualizer.git
   ```
2. Install pip packages (listed in prerequisites)
   ```sh
   pip install
   ```

<!-- USAGE EXAMPLES -->
## Usage

1. Start with placing the CSV data files into the folder 'logData.'
2. All CSV files MUST follow a naming convention.
   
     - _Name Template: 'GraphType_Parameter_TransmissionRate_FPS_TransmitterOrReceiverID.csv'_
        * _ID_ is an nonnegative integer that pairs together corresponding transmitter and receiver files.
    -  _Name Example: 'temperature_40c_25Hz_100fps_receiver1.csv'_

    - _Pair Example: (Transmitter): 'transmissionrate_50Hz_50Hz_100fps_transmitter4.csv'_
    - _Pair Example: (Receiver): 'transmissionrate_50Hz_50Hz_100fps_receiver4.csv'_

   
    <img src="https://github.com/sam-shridhar1950f/ber-visualizer/blob/photos/folderStructure.PNG?raw=true"></img>
3. Run **graph.py.**
<br>
<img src="https://github.com/sam-shridhar1950f/ber-visualizer/blob/photos/terminal.PNG?raw=true"></img>
4. Select your graph option. 
         <br>
         <br>
          - 'transmissionrate', 'temperature', 'pH', 'turbidity', 'salinity' will graph the BER of all data files within the respective category.
           <br>
           <br>
          - 'average' will display a graph with the average BER of every category existing in the logData directory
<br>
<br>
<img src="https://github.com/sam-shridhar1950f/ber-visualizer/blob/photos/graph.png?raw=true"></img>
5. The graph will generate.
   





<!-- ROADMAP -->
## Customization

- Open the **config.json** file to change the precision variable of the BER calculation.



