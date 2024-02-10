{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyOVTixr3qnFeMj9HclHRf1+",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/Shavva-Satya196/3_Frames_Lab/blob/main/3Frames.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "JBv5dMpoo0FC"
      },
      "outputs": [],
      "source": [
        "\"\"\"Problem-2:\n",
        "Build a word count application, where the constraints are that you have 10 MB RAM and 1\n",
        "GB text file. You should be able to efficiently parse the text file and output the words and\n",
        "counts in a sorted way. Write a program to read a large file, and emit the sorted words along\n",
        "with the count. Try to implement fuzzy search as well (fix the spelling issues) Algorithm\n",
        "should have Log N complexity.\"\"\""
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "Suppose we have to sort a 1GB file of random integers and the available ram size is 200 Mb, how will it be done?\n",
        "\n",
        "The easiest way to do this is to use external sorting.\n",
        "We divide our source file into temporary files of size equal to the size of the RAM and first sort these files.\n",
        "Assume 1GB = 1024MB, so we follow following steps.\n",
        "\n",
        "Divide the source file into 5 small temporary files each of size 200MB (i.e., equal to the size of ram).\n",
        "Sort these temporary files one bye one using the ram individually (Any sorting algorithm : quick sort, merge sort)."
      ],
      "metadata": {
        "id": "mqv3YVHfph1t"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "from collections import defaultdict\n",
        "import heapq\n",
        "import re\n",
        "\n",
        "def split_file(file_path, chunk_size=10*1024*1024):\n",
        "    with open(file_path, 'r', encoding='utf-8') as file:\n",
        "        while True:\n",
        "            chunk = file.read(chunk_size)\n",
        "            if not chunk:\n",
        "                break\n",
        "            yield chunk\n",
        "\n",
        "def count_words(chunk):\n",
        "    word_counts = defaultdict(int)\n",
        "    words = re.findall(r'\\b\\w+\\b', chunk.lower())\n",
        "    for word in words:\n",
        "        word_counts[word] += 1\n",
        "    return word_counts\n",
        "\n",
        "def merge_counts(counts):\n",
        "    merged_counts = defaultdict(int)\n",
        "    for count in counts:\n",
        "        for word, freq in count.items():\n",
        "            merged_counts[word] += freq\n",
        "    return merged_counts\n",
        "\n",
        "def fuzzy_search(word, word_counts):\n",
        "    word=word.lower()\n",
        "    return [key for key in word_counts.keys() if key.startswith(word)]\n",
        "\n",
        "def main(file_path):\n",
        "    counts = []\n",
        "    for chunk in split_file(file_path):\n",
        "        counts.append(count_words(chunk))\n",
        "\n",
        "    word_counts = merge_counts(counts)\n",
        "    sorted_word_counts = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)\n",
        "\n",
        "    # Output sorted words and counts\n",
        "    for word, count in sorted_word_counts:\n",
        "        print(f\"{word}: {count}\")\n",
        "\n",
        "    # Example fuzzy search\n",
        "    print(\"Fuzzy Search:\")\n",
        "    search_word = \"ADD\"\n",
        "    suggestions = fuzzy_search(search_word, word_counts)\n",
        "    print(f\"Suggestions for '{search_word}': {suggestions}\")\n",
        "\n",
        "if __name__ == \"__main__\":\n",
        "    file_path = \"/content/sampcod.txt\"\n",
        "    main(file_path)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "940B_YZXo9cE",
        "outputId": "6a0febc7-a057-40b7-c64b-ed30dbefed18"
      },
      "execution_count": 3,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "the: 14\n",
            "product: 9\n",
            "electronics: 5\n",
            "dog: 5\n",
            "products: 4\n",
            "fox: 4\n",
            "cat: 4\n",
            "over: 3\n",
            "tracker: 3\n",
            "tree: 3\n",
            "db: 2\n",
            "laptop: 2\n",
            "smartphone: 2\n",
            "connectivity: 2\n",
            "headphones: 2\n",
            "activity: 2\n",
            "with: 2\n",
            "heart: 2\n",
            "rate: 2\n",
            "monitor: 2\n",
            "water: 2\n",
            "resistant: 2\n",
            "gps: 2\n",
            "tracking: 2\n",
            "backpack: 2\n",
            "for: 2\n",
            "running: 2\n",
            "shoes: 2\n",
            "to: 2\n",
            "brown: 2\n",
            "jumps: 2\n",
            "lazy: 2\n",
            "at: 2\n",
            "productdatabase: 1\n",
            "list: 1\n",
            "of: 1\n",
            "high: 1\n",
            "performance: 1\n",
            "16gb: 1\n",
            "ram: 1\n",
            "512gb: 1\n",
            "ssd: 1\n",
            "latest: 1\n",
            "model: 1\n",
            "6: 1\n",
            "7: 1\n",
            "display: 1\n",
            "5g: 1\n",
            "noise: 1\n",
            "cancelling: 1\n",
            "ear: 1\n",
            "design: 1\n",
            "bluetooth: 1\n",
            "latness: 1\n",
            "fashion: 1\n",
            "stylish: 1\n",
            "everyday: 1\n",
            "use: 1\n",
            "multiple: 1\n",
            "compartments: 1\n",
            "padded: 1\n",
            "straps: 1\n",
            "sports: 1\n",
            "lightweight: 1\n",
            "breathable: 1\n",
            "mesh: 1\n",
            "cushioned: 1\n",
            "sole: 1\n",
            "fitye: 1\n",
            "add: 1\n",
            "database: 1\n",
            "in: 1\n",
            "add_product: 1\n",
            "smart: 1\n",
            "quick: 1\n",
            "sleeps: 1\n",
            "under: 1\n",
            "a: 1\n",
            "chases: 1\n",
            "fence: 1\n",
            "meows: 1\n",
            "barks: 1\n",
            "and: 1\n",
            "play: 1\n",
            "together: 1\n",
            "sun: 1\n",
            "sets: 1\n",
            "behind: 1\n",
            "provides: 1\n",
            "shade: 1\n",
            "Fuzzy Search:\n",
            "Suggestions for 'ADD': ['add', 'add_product']\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "\"\"\"Problem-3:\n",
        "Come up with an approach for product configuration, where multiple products can be\n",
        "stored. Build an in-memory database or in-memory storage. We should be able to have\n",
        "product categories along with product descriptions and details. We should be able to store a\n",
        "wide range of types of products similar to Amazon, we should be able to implement efficient\n",
        "search of the products and flexible configuration of the products. In addition to in-memory\n",
        "storage, build an efficient textual search on any of the parameters (similar to search in\n",
        "Amazon).\"\"\""
      ],
      "metadata": {
        "id": "0qaA_KjurULg"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "class Product:\n",
        "    def __init__(self, name, category, description, details):\n",
        "        self.name = name\n",
        "        self.category = category\n",
        "        self.description = description\n",
        "        self.details = details\n",
        "\n",
        "class Category:\n",
        "    def __init__(self, name):\n",
        "        self.name = name\n",
        "        self.products = []\n",
        "\n",
        "class ProductDatabase:\n",
        "    def __init__(self):\n",
        "        self.products = {}\n",
        "        self.categories = {}\n",
        "\n",
        "    def add_product(self, product):\n",
        "        self.products[product.name] = product\n",
        "        if product.category not in self.categories:\n",
        "            self.categories[product.category] = Category(product.category)\n",
        "        self.categories[product.category].products.append(product)\n",
        "\n",
        "    def search_products(self, query):\n",
        "        results = []\n",
        "        for product in self.products.values():\n",
        "            if query.lower() in product.name.lower() or \\\n",
        "               query.lower() in product.category.lower() or \\\n",
        "               query.lower() in product.description.lower() or \\\n",
        "               query.lower() in product.details.lower():\n",
        "                results.append(product)\n",
        "        return results\n",
        "\n",
        "db = ProductDatabase()\n",
        "\n",
        "# List of products\n",
        "products = [\n",
        "    Product(\"Laptop\", \"Electronics\", \"High-performance laptop\", \"16GB RAM, 512GB SSD\"),\n",
        "    Product(\"Smartphone\", \"Electronics\", \"Latest smartphone model\", \"6.7'' display, 5G connectivity\"),\n",
        "    Product(\"Headphones\", \"Electronics\", \"Noise-cancelling headphones\", \"Over-ear design, Bluetooth connectivity\"),\n",
        "    Product(\"Fitness Tracker\", \"Electronics\", \"Activity tracker with heart rate monitor\", \"Water-resistant, GPS tracking\"),\n",
        "    Product(\"Backpack\", \"Fashion\", \"Stylish backpack for everyday use\", \"Multiple compartments, padded straps\"),\n",
        "    Product(\"Running Shoes\", \"Sports\", \"Lightweight running shoes\", \"Breathable mesh, cushioned sole\"),\n",
        "    Product(\"Fitye \", \"Electronics\", \"Activity tracker with heart rate monitor\", \"Water-resistant, GPS tracking\")\n",
        "]\n",
        "\n",
        "# Add products to the database\n",
        "for product in products:\n",
        "    db.add_product(product)\n",
        "# Search for products\n",
        "results = db.search_products(\"Fit\")\n",
        "for product in results:\n",
        "    print(f\"Name: {product.name}, Category: {product.category}, Description: {product.description}\")S"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "zsjwVlZzrZJx",
        "outputId": "348680cf-32ac-4ef9-d261-fc078434be7b"
      },
      "execution_count": 9,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Name: Fitness Tracker, Category: Electronics, Description: Activity tracker with heart rate monitor\n",
            "Name: Fitye , Category: Electronics, Description: Activity tracker with heart rate monitor\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "cIXoXNnorbk2"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}