# LSH-Minhash
LSH implementation using Minhash on congressional voting record dataset
The CVR R script does the necessary preprocessing of the dataset. The dummies package is used to create dummy variables
to indicate yes, no or a NA vote by a congressman/congresswoman.

The Mihhash implementation requires a choice of number of hash functions and the band to begin with. This is solved by
selecting a threshold level of similarity. Objects with greater than this threhold are expected to cluster together.

An approximation to the performance of the banding scheme (see Ullman Rajaraman's MMDS text) indicates that the cutover
point in the curve is approximated by (1r) ** (1/b) where r is the number of hash functions and b is the number of bands
If we choose r = 16 and b  = 4, then the above expression evaluates to 0.5.

This means objects with greater than 0.5 Jaccard Similarity are expected to hash together with this design. This is the
level of similarity used in this implementation.

The algorithm is essentially encoded in the min_hash() method and the details of the implementation are as per the
description in the MMDS text.
