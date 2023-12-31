.. _vector_databases:

Vector Databases
================

Vector databases are useful for querying unstructured data. A vector index contains the vectors (embeddings) generated by processing the unstructured data using a feature extractor function. While processing a query, EvaDB uses the vector index to retrieve the vectors most akin to the embedded query, which is again obtained by passing the user's query through the same feature extractor function. This retrieval process is accelerated by a vector store.

Here is a list of supported vector stores in EvaDB. 

.. note::
   A comprehensive benchmark of vector databases in EvaDB is available in this `page <https://medium.com/evadb-blog/how-to-pick-a-vector-database-quantitative-analysis-afae5ea9e5b1>`_.

.. tableofcontents::