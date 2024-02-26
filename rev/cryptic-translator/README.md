# Crpytic Translator

## Description

Imagine a world where your data goes through a distributed cryptic translator, transforming your clear, concise messages into a jumbled mess that only the most seasoned cryptographers could hope to decipher. It's like being trapped in a maze of encryption, where every turn leads to another layer of confusion. Picture yourself as the protagonist in a tech-savvy thriller, where the fate of the world hinges on your ability to crack the code before the deadline. With every byte of information transformed into a cryptic puzzle, it's a race against time worthy of a Hollywood blockbuster. Just when you thought you had it figured out, a twist worthy of M. Night Shyamalan leaves you questioning everything you thought you knew about data security. Welcome to the distributed cryptic translator - where clarity goes to die and complexity reigns supreme.

Note: Wrap the flag in BITSCTF{}

## Writeup

Reviewing the code and the challenge description reveals that the encoder utilizes multiple servers to encode the message. There are two types of servers indicated in [main.go](./main.go), one of which is a listener server.

The cluster formation is facilitated by the [memberlist](https://pkg.go.dev/github.com/hashicorp/memberlist) library. Let's delve into each type of server.

Examining the `ListerNode` function in [listener.go](./listener.go), the initial part configures the settings according to the `memberlist` documentation. The subsequent part establishes a watcher responsible for monitoring file changes on the specified filepath (`flag.txt`) and transmitting the content of that file to the cluster. The comment suggests that the writer triggers the save command after inputting each character into the file.

Next, inspect the `ForwardToCluster` function in [helper.go](./helper.go). It first retrieves the list of cluster nodes and sorts them based on their port numbers. Then, it determines the index in the node list to which the message should be sent. The data is encoded using the `parseData` function and subsequently forwarded to the next node.

Therefore, `parseData` is employed for encoding. It processes each byte of the provided data, swapping the upper and lower nibbles and converting the byte into a binary string. The 0s and 1s in this binary string are replaced by characters from the string `sudeepbaudha`, selected based on the node number.

The comment in [main.go](./main.go) suggests that the encoder employs 5 nodes and 1 listener node.

Once the message reaches the last node, it is redirected back to the listener node. Upon receiving the message, the `NotifyMsg` event is triggered in the `memberlist`. When the listener node receives the final encoded message, it appends it to `output`.

In summary, there is a cluster of 6 nodes sequentially transmitting the data from node 0 to node 1, and so on until node 5, with the data being encoded before each transmission. Therefore, reversing the `parseData` function and executing it 6 times should decode the text.

[solver.py](./solver.py) provides a rudimentary implementation of the reversed `parseData` function.

**Note: The encoded file can be found in the zip folder.**

## Flag
`BITSCTF{ppprpr0pr0_pr0_dpr0_depr0_decpr0_dec0pr0_dec0d3pr0_dec0d3rrpr0_dec0d3rrrpr0_dec0d3rpr0_dec0dpprpr0pr0_pr0_dpr0_depr0_decpr0_dec0pr0_dec0d3pr0_dec0d3rrprppr0_dec0d3rrrpr0_dpr0_depr0_decpr0_dec0pr0_dec0d3pr0_dec0d3rrpprpr0_dec0d3rrrpr0_pr0_dpr0_depr0_decpr0_dec0pr0_dec0d3pr0_dec0d3rrprppr0_dec0d3rrrpr0_dpr0_depr0_decpr0_dec0pr0_dec0d3pr0_dec0d3rrprppr0_dec0d3rrrpr0_dpr0_depr0_decpr0_dec0pr0_dec0d3pr0_dec0d3rrpprpr0_dec0d3rrrpr0_pr0_dpr0_depr0_decpr0_dec0pr0_dec0d3pr0_dec0d3rrpr0_dec0d3rrrpr0_dec0d3rpr0_dec0dpr0pr0_dec0d3rpr0_dec0dpr0_pr0pr0_dec0d3rpr0_dec0dpr0_pr0pr0_dec0d3rpr0_dec0dpr0pr0_dec0d3rpr0_dec0dpr0_pr0pr0_dec0d3rpr0_dec0d}`

## Author

[**@InimicalX**](https://github.com/Akhil2193)