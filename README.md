# BDO-MARKET-API
 Python Library for Black Desert Online marketplace.

[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]



<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#resources">Resources</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
    </li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>


<!-- ABOUT THE PROJECT -->
## About The Project

Thanks to :sparkles:[Ruwann](https://github.com/Ruwann):sparkles: for helping me figure out how to read the Google console.

I tried to build a Python library to communicate with the Black Desert Online marketplace.

### Resources
* [curlconverter](https://github.com/NickCarneiro/curlconverter) by NickCarneiro
* [bdo-marketplace](https://github.com/kookehs/bdo-marketplace)  by kookehs


## Getting Started

Obtaining API credentials is analogous to the explanation provided by [kookehs](https://github.com/kookehs/bdo-marketplace#obtaining-credentials-for-api-calls). However, I used an external tool called [curlconverter](https://curl.trillworks.com/) to convert the cURL to a Python script and worked from there.
I will sort-off copy-paste it here for convencience.


0. `User-Agent` is already spoofed within the library. No need for you to do this.
1. Sign in to https://market.blackdesertonline.com/.
2. Open the `Developer Tools` and select `Network`.
3. Click the search icon. Search for an item with enhancement. 
4. Click on the listing to open up details for that item.
5. Check the network tab for `GetItemSellBuyInfo`. 
	- Create a file `secrets.py` with parameters `SESSIONID`, `COOKIETOKEN` and `FORMTOKEN`. An example can be found [here]5https://github.com/JeroenProoth/BDO-MARKET-API/blob/main/examples/secrets_example.py°.
	- Right-click and select `cURL (cmd)`
	- Paste into [curlconverter](https://curl.trillworks.com/] and convert to Python).
		- `SESSIONID` can be found under `cookies`, and is called `ASP.NET_SessionId`
		- `COOKIETOKEN` can be found under `cookies` and is called `__RequestVerificationToken`
		- `FORMTOKEN` can be found under `headers` and is called `__RequestVerificationToken`



## Contact

[![Issues][issues-shield]][issues-url]

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/JeroenProoth/BDO-MARKET-API.svg?style=for-the-badge
[contributors-url]: https://github.com/JeroenProoth/BDO-MARKET-API/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/JeroenProoth/BDO-MARKET-API.svg?style=for-the-badge
[forks-url]: https://github.com/JeroenProoth/BDO-MARKET-API/network/members
[stars-shield]: https://img.shields.io/github/stars/JeroenProoth/BDO-MARKET-API.svg?style=for-the-badge
[stars-url]: https://github.com/JeroenProoth/BDO-MARKET-API/stargazers
[issues-shield]: https://img.shields.io/github/issues/JeroenProoth/BDO-MARKET-API.svg?style=for-the-badge
[issues-url]: https://github.com/JeroenProoth/BDO-MARKET-API/issues

