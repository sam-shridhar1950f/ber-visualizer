# ber-visualizer




  <h3 align="center">BER Visualizer</h3>

  <p align="center">
    A graph-generator that can process large amounts of VLC data and return a graph comparing BERs (Bit Error Rates).
    <br />
  </p>
</p>

### Prerequisites

This is an example of how to list things you need to use the software and how to install them.
* pip
  ```sh
  pip install pandas
  pip install matplotlib
  ```

### Installation

1. Get a free API Key at [https://example.com](https://example.com)
2. Clone the repo
   ```sh
   git clone https://github.com/sam-shridhar1950f/ber-visualizer.git
   ```
3. Install pip packages (listed in prerequisites)
   ```sh
   pip install
   ```

<!-- USAGE EXAMPLES -->
### Usage

1. Start with placing the CSV data files into the folder 'logData.'
2. All CSV files MUST follow a naming convention.
   
     - _Name Template: 'GraphType_Parameter_TransmissionRate_FPS_TransmitterOrReceiverID.csv'_
        * _ID_ is an nonnegative integer that pairs together corresponding transmitter and receiver files.
    -  _Name Example: 'temperature_40c_25Hz_100fps_receiver1.csv'_

    - _Pair Example: (Transmitter): 'transmissionrate_50Hz_50Hz_100fps_transmitter4.csv'_
    - _Pair Example: (Receiver): 'transmissionrate_50Hz_50Hz_100fps_receiver4.csv'_

   
    <img src="https://github.com/sam-shridhar1950f/ber-visualizer/blob/photos/folderStructure.PNG?raw=true">
3. Run **graph.py.**
<img src="https://github.com/sam-shridhar1950f/ber-visualizer/blob/photos/terminal.PNG?raw=true">
4. Select your graph option. 
   - 'transmissionrate', 'temperature', 'pH', 'turbidity', 'salinity' will graph the BER of all data files within the respective category.
   - 'average' will display a graph with the average BER of every category existing in the logData directory
<img src="https://github.com/sam-shridhar1950f/ber-visualizer/blob/photos/graph.png?raw=true">
5. The graph will generate!
   

_For more examples, please refer to the [Documentation](https://example.com)_



<!-- ROADMAP -->
## Roadmap

See the [open issues](https://github.com/othneildrew/Best-README-Template/issues) for a list of proposed features (and known issues).



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.



<!-- CONTACT -->
## Contact

Your Name - [@your_twitter](https://twitter.com/your_username) - email@example.com

Project Link: [https://github.com/your_username/repo_name](https://github.com/your_username/repo_name)



<!-- ACKNOWLEDGEMENTS -->
## Acknowledgements
* [GitHub Emoji Cheat Sheet](https://www.webpagefx.com/tools/emoji-cheat-sheet)
* [Img Shields](https://shields.io)
* [Choose an Open Source License](https://choosealicense.com)
* [GitHub Pages](https://pages.github.com)
* [Animate.css](https://daneden.github.io/animate.css)
* [Loaders.css](https://connoratherton.com/loaders)
* [Slick Carousel](https://kenwheeler.github.io/slick)
* [Smooth Scroll](https://github.com/cferdinandi/smooth-scroll)
* [Sticky Kit](http://leafo.net/sticky-kit)
* [JVectorMap](http://jvectormap.com)
* [Font Awesome](https://fontawesome.com)





<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/othneildrew/Best-README-Template.svg?style=for-the-badge
[contributors-url]: https://github.com/othneildrew/Best-README-Template/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/othneildrew/Best-README-Template.svg?style=for-the-badge
[forks-url]: https://github.com/othneildrew/Best-README-Template/network/members
[stars-shield]: https://img.shields.io/github/stars/othneildrew/Best-README-Template.svg?style=for-the-badge
[stars-url]: https://github.com/othneildrew/Best-README-Template/stargazers
[issues-shield]: https://img.shields.io/github/issues/othneildrew/Best-README-Template.svg?style=for-the-badge
[issues-url]: https://github.com/othneildrew/Best-README-Template/issues
[license-shield]: https://img.shields.io/github/license/othneildrew/Best-README-Template.svg?style=for-the-badge
[license-url]: https://github.com/othneildrew/Best-README-Template/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/othneildrew
[product-screenshot]: images/screenshot.png

