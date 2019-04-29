# Tigers_v_Goats

*** Rules of the Game:

Tigers and Goats using a neural network.

This is an asymmetric strategy game, with one player controlling 3 tigers and another controlling up to 15 goats on the board we drew up last Fri.

1. The game begins with the three tigers on board. Goat plays first.

2. For the first 15 rounds, one goat is placed on the board (prior goats cannot be moved at this stage). The tigers move according to their rules, including eating goats if possible.

3. Once the goats are placed, both the tigers and goats move.

4. Tigers and goats can move to any adjacent empty position.

5. Tigers can jump over one goat to eat them. They cannot jump over more than one goat.

6. Goats win by stalemating the tigers---namely, no tiger has a valid move left. Tigers win by eating 6 goats.

*** Tasks:

1. Program the game in python to generate all valid moves for each player at any step. Test this by playing the game.

2. Generate learning data by choosing random configurations of the game, followed by evaluating moves. This is not
   quite a supervised learning setup since we do not know which move is best. Rather, keep track of how good positions
   are by using the number of valid moves for the tigers and the number of goats on the board.

3. We use this rough data to train the network. We will then iterate over refining positions/data to improve training.