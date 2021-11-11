MS2ChemClass -- a tool to perform chemical compound classification based on mass spectrum by using embeddings.  

1. General workflows:  
    1) Mass spectra from GNPS --- (matchms) ---> mass spectra with positive ion and unique InChIKey --- (Spec2Vec) ---> mass spectral embeddings.  
    2) Use mass spectral embeddings with ClassyFire and PClassifier ontologies to do classification by LDA and Random Forest.  
                12 situations: LDA in Class level in ClassyFire ontology;  
                               LDA in Superclass level in ClassyFire ontology;  
                               LDA in Subclass level in ClassyFire ontology;  
                               LDA in Class level in NPClassifier ontology;  
                               LDA in Superclass level in NPClassifier ontology;  
                               LDA in Pathway level in NPClassifier ontology;  
                               Random Forest in Class level in ClassyFire ontology;  
                               Random Forest in Superclass level in ClassyFire ontology;  
                               Random Forest in Subclass level in ClassyFire ontology;  
                               Random Forest in Class level in NPClassifier ontology;  
                               Random Forest in Superclass level in NPClassifier ontology;  
                               Random Forest in Pathway level in NPClassifier ontology.  
     3) Compare the accuracy per classes in one situation. Explore the relationship among class accuracy, group size, and Internal Jaccard Similarity.  
     4) Compare the performance between LDA and Random Forest in the same class level and the same ontology.  
     5) Select "good" performed classes (with high accuracy and sufficient group size to avoid overfitting).  
     6) Compare MS2ChemClass and CANOPUS based on run-time and class accuracies.  

2. Tools required before using MS2ChemClass:  
  Python 3.8.10  
  sklearn 0.24.1 -- used for LDA and Random Forest classification.  
  matchms 0.8.1 -- used for processing mass spectra data, e.g. selecting the mass spectra with positive ion and unique InChIKey.  
  Spec2Vec 0.5.0 -- use mass spectra data to build spectral embeddings.   
  seaborn 0.11.1 --  used for constructing bar plots to compare accuracy, group size, and Internal Jaccard similarity.  
  matplotlib 3.3.4 -- Ploting tools.    
  gensim 4.0.1  -- combined with Spec2Vec to create mass spectral embedding vectors.  
  scipy 1.6.2 -- used for calculation of internal jaccard similarity.  
  pandas 1.2.4 -- used for data frame.  
  numpy 1.20.1 -- used for array.  

3. Compared with CANOPUS:  
  Tool: SIRIUS 4.9.5  
  Code in command line: $sirius -i <input_name>.mgf -o <output_dir> formula zodiac structure canopus  
  
