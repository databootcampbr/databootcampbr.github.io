title: Como instalar o PySpark no Jupyter
slug: como-instalar-o-pyspark-no-jupyter
category: setup
date: 2017-10-08
modified: 2017-10-08


O [Spark](https://spark.apache.org/) é uma poderosa ferramenta de processamento paralelo que pode ser usada para paralelizar de forma fácil suas análises ou jobs em BigData.

## Dependência

Como dependência precisa instalar o [Java](https://java.com/pt_BR/download/). No [próprio site do Java](https://www.java.com/en/download/help/download_options.xml) você tem detalhado como instalar em cada sistema operacional.

## Instalação

Sua última versão pode ser instalada de forma fácil digitando no notebook:

```
  !pip install pyspark
```

ou buscando no anaconda pelo pacote **pyspark** e instalando.

Depois disso, já pode criar sua sessão do Spark de forma simples no seu notebook:

```
  from pyspark.sql import SparkSession

  spark = SparkSession.builder.master("local") \
            .appName("DataBootcamp") \
            .getOrCreate()
```

## Extra

Caso precise do spark completo pode fazer download da sua última versão no [site oficial](https://spark.apache.org/downloads.html), descompactar e colocar a variável **SPARK_HOME** como o *path* de onde você extraiu. Depois utilize o [findspark](https://github.com/minrk/findspark) para carregar ele dentro do [Jupyter Notebook](https://nbviewer.jupyter.org/).
