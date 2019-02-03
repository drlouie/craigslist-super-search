# craigslist-super-search

* [Craigslist SuperSearch](https://github.com/drlouie/craigslist-super-search)
* [Use It Online, Create an Account](https://myvirtualprivate.com/craigslist)

Craigslist SuperSearch(CLSS) is a Craigslist multi-location and full-state search program written in Perl, tested on UNIX FreeBSD 8.2, FreeBSD 11, WAMP, LAMP and other UNIX and Linux servers, virtual, hosted, local and otherwise.

Created by Luis G. Rodriguez (doctorlouie), in 2010, it hasn't quite been updated much at all since it was originally written, however its been highly instrumental with my marketing and market research efforts. Furthermore, its quite the nifty tool for quickly searching large swaths of areas for specific tangible and intagible goods I'm seeking to acquire. Feel free to help build it into something much more effective and efficient. I've just gotten used to it as it sits, however I'd love to see it progress immensely, which is why its being released under the MIT License.

### Installing Craigslist SuperSearch
Upload to web server, local or otherwise. Move to web-root directory and extract issuing the following command:

* tar -xf craigslist.tar

Then simply run your favorite browser to use Craigslist SuperSearch directly from your web server. Please make certain to report any bugs or updates back to me. And, by all means, contribute back to this project at your leisure.

### Perl Module Dependencies
* LWP::Simple
* CGI
* CGI::Carp
* HTML::SimpleLinkExtor
* HTML::TokeParser
* HTML::ResolveLink
* Text::Autoformat

### TODO List

1. International support, currently only supports US States and Territories.
2. Client-based data retrieval, instead of relying on server for document retrieval and processing. Why? Craigslist will block an IP running too many consecutive searches, in essence anything they find to be of automated or bot-based nature, this, I'm sure, is to keep from being bombarded by automated requests. The block is usually no longer than 24 hours, based on my working research, as to how many consecutive(multiple searches across multiple areas of a State within say 1-3 minutes of each other) searches constitute too much, well I haven't quite found that figure yet. Therefore, if we rely on client to retrieve document we can then have that data be forwarded to the server for processing. This will help mitigate any issues with a sever not being able to run CLSS, considering its IP Address can be blocked when mass amounts of queries are being shoved through Craigslist search. 

## License

See the [LICENSE](LICENSE.md) file for license rights and limitations (MIT).
