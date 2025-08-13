{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": []
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
      "cell_type": "code",
      "source": [
        "!apt-get install sqlite3"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "nXfWqLU2PdMw",
        "outputId": "cb6c1f0b-68b4-478e-cf7a-fda62a0ecfba"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Reading package lists... Done\n",
            "Building dependency tree... Done\n",
            "Reading state information... Done\n",
            "Suggested packages:\n",
            "  sqlite3-doc\n",
            "The following NEW packages will be installed:\n",
            "  sqlite3\n",
            "0 upgraded, 1 newly installed, 0 to remove and 35 not upgraded.\n",
            "Need to get 769 kB of archives.\n",
            "After this operation, 1,874 kB of additional disk space will be used.\n",
            "Get:1 http://archive.ubuntu.com/ubuntu jammy-updates/main amd64 sqlite3 amd64 3.37.2-2ubuntu0.5 [769 kB]\n",
            "Fetched 769 kB in 0s (2,588 kB/s)\n",
            "Selecting previously unselected package sqlite3.\n",
            "(Reading database ... 126284 files and directories currently installed.)\n",
            "Preparing to unpack .../sqlite3_3.37.2-2ubuntu0.5_amd64.deb ...\n",
            "Unpacking sqlite3 (3.37.2-2ubuntu0.5) ...\n",
            "Setting up sqlite3 (3.37.2-2ubuntu0.5) ...\n",
            "Processing triggers for man-db (2.10.2-1) ...\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 1,
      "metadata": {
        "id": "FAj0NbuArOXH"
      },
      "outputs": [],
      "source": [
        "import sqlite3\n",
        "\n",
        "def init_db():\n",
        "    conn = sqlite3.connect(\"receipts.db\")\n",
        "    cursor = conn.cursor()\n",
        "    cursor.execute(\"\"\"\n",
        "        CREATE TABLE IF NOT EXISTS receipts (\n",
        "            id INTEGER PRIMARY KEY AUTOINCREMENT,\n",
        "            raw_text TEXT,\n",
        "            category TEXT,\n",
        "            date TEXT,\n",
        "            amount REAL\n",
        "        )\n",
        "    \"\"\")\n",
        "    conn.commit()\n",
        "    conn.close()\n",
        "\n",
        "def insert_receipt(raw_text, category, date, amount):\n",
        "    init_db()\n",
        "    conn = sqlite3.connect(\"receipts.db\")\n",
        "    cursor = conn.cursor()\n",
        "    cursor.execute(\n",
        "        \"INSERT INTO receipts (raw_text, category, date, amount) VALUES (?, ?, ?, ?)\",\n",
        "        (raw_text, category.strip(), date, amount)\n",
        "    )\n",
        "    conn.commit()\n",
        "    conn.close()\n"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "insert_receipt(\"Big Bazaar\", \"Groceries\", \"2025-08-09\", 1250.50)\n",
        "insert_receipt(\"Amazon\", \"Electronics\", \"2025-08-10\", 4999.99)\n",
        "insert_receipt(\"Big Bazaar - TATA SAMPANN DAL 1KG, FORTUNE OIL 1L\", \"Groceries\", \"2025-08-01\", 1250.50)\n",
        "insert_receipt(\"Amazon - Sony Headphones WH-1000XM4\", \"Electronics\", \"2025-08-02\", 24990.00)\n",
        "insert_receipt(\"Swiggy - Pizza Hut Veggie Supreme\", \"Food\", \"2025-08-03\", 599.00)\n",
        "insert_receipt(\"Flipkart - HP Pavilion Laptop 15\", \"Electronics\", \"2025-08-04\", 59990.00)\n",
        "insert_receipt(\"Uber - Airport Drop\", \"Transport\", \"2025-08-05\", 450.00)\n",
        "insert_receipt(\"Reliance Digital - Samsung Galaxy S23\", \"Electronics\", \"2025-08-06\", 79999.00)\n",
        "insert_receipt(\"Myntra - Nike Running Shoes\", \"Fashion\", \"2025-08-07\", 4999.00)\n",
        "insert_receipt(\"Domino's - Cheese Burst Pizza\", \"Food\", \"2025-08-08\", 799.00)\n",
        "insert_receipt(\"BookMyShow - Oppenheimer IMAX Ticket\", \"Entertainment\", \"2025-08-09\", 350.00)\n",
        "insert_receipt(\"D-Mart - Rice 10KG, Oil 5L\", \"Groceries\", \"2025-08-10\", 1890.75)\n",
        "insert_receipt(\"Zomato - Biryani by Kilo\", \"Food\", \"2025-08-11\", 899.00)\n",
        "insert_receipt(\"Apple Store - MacBook Air M3\", \"Electronics\", \"2025-08-12\", 114900.00)\n",
        "insert_receipt(\"H&M - Denim Jacket\", \"Fashion\", \"2025-08-13\", 2999.00)\n",
        "insert_receipt(\"Spencers - Vegetables & Fruits\", \"Groceries\", \"2025-08-14\", 745.20)\n",
        "insert_receipt(\"MakeMyTrip - Goa Flight Ticket\", \"Travel\", \"2025-08-15\", 5499.00)\n",
        "insert_receipt(\"Tanishq - Gold Chain\", \"Jewellery\", \"2025-08-16\", 32500.00)\n",
        "insert_receipt(\"Metro Shoes - Formal Leather Shoes\", \"Fashion\", \"2025-08-17\", 3499.00)\n",
        "insert_receipt(\"Lifestyle - Perfume Set\", \"Fashion\", \"2025-08-18\", 1599.00)\n",
        "insert_receipt(\"Crossword - Atomic Habits Book\", \"Books\", \"2025-08-19\", 499.00)\n",
        "insert_receipt(\"Samsung Store - 55 Inch QLED TV\", \"Electronics\", \"2025-08-20\", 75990.00)\n",
        "insert_receipt(\"Levi's - Slim Fit Jeans\", \"Fashion\", \"2025-08-21\", 2799.00)\n",
        "insert_receipt(\"Woodland - Trekking Shoes\", \"Fashion\", \"2025-08-22\", 4499.00)\n",
        "insert_receipt(\"Nykaa - Skincare Combo\", \"Beauty\", \"2025-08-23\", 1899.00)\n",
        "insert_receipt(\"Croma - Bluetooth Speaker\", \"Electronics\", \"2025-08-24\", 4990.00)\n",
        "insert_receipt(\"Pantaloons - Summer Dress\", \"Fashion\", \"2025-08-25\", 1799.00)\n",
        "insert_receipt(\"Haldiram's - Snacks & Sweets\", \"Food\", \"2025-08-26\", 1090.00)\n",
        "insert_receipt(\"Tata Cliq - Smartwatch\", \"Electronics\", \"2025-08-27\", 8999.00)\n",
        "insert_receipt(\"PVR Cinemas - Barbie Movie Ticket\", \"Entertainment\", \"2025-08-28\", 300.00)\n",
        "insert_receipt(\"Cafe Coffee Day - Cappuccino & Sandwich\", \"Food\", \"2025-08-29\", 350.00)\n",
        "insert_receipt(\"Ola - Office Ride\", \"Transport\", \"2025-08-30\", 220.00)\n",
        "insert_receipt(\"Paytm Mall - Wireless Mouse\", \"Electronics\", \"2025-08-31\", 799.00)\n",
        "insert_receipt(\"Westside - Formal Shirt\", \"Fashion\", \"2025-09-01\", 1299.00)\n",
        "insert_receipt(\"Burger King - Whopper Meal\", \"Food\", \"2025-09-02\", 299.00)\n",
        "insert_receipt(\"Pepperfry - Study Table\", \"Furniture\", \"2025-09-03\", 5999.00)\n",
        "insert_receipt(\"Urban Ladder - Sofa Set\", \"Furniture\", \"2025-09-04\", 28990.00)\n",
        "insert_receipt(\"Decathlon - Gym Bag\", \"Sports\", \"2025-09-05\", 899.00)\n",
        "insert_receipt(\"Adidas - Sports T-shirt\", \"Fashion\", \"2025-09-06\", 1499.00)\n",
        "insert_receipt(\"Starbucks - Latte & Brownie\", \"Food\", \"2025-09-07\", 550.00)\n",
        "insert_receipt(\"FirstCry - Baby Diapers\", \"Baby Care\", \"2025-09-08\", 750.00)\n",
        "insert_receipt(\"Vijay Sales - Air Conditioner\", \"Electronics\", \"2025-09-09\", 34990.00)\n",
        "insert_receipt(\"FabIndia - Cotton Kurta\", \"Fashion\", \"2025-09-10\", 1999.00)\n",
        "insert_receipt(\"Big Basket - Monthly Groceries\", \"Groceries\", \"2025-09-11\", 4350.00)\n",
        "insert_receipt(\"Bata - Casual Sneakers\", \"Fashion\", \"2025-09-12\", 1899.00)\n",
        "insert_receipt(\"Titan - Analog Watch\", \"Accessories\", \"2025-09-13\", 6499.00)\n",
        "insert_receipt(\"Shoppers Stop - Handbag\", \"Fashion\", \"2025-09-14\", 2999.00)\n",
        "insert_receipt(\"Columbia Sportswear - Jacket\", \"Fashion\", \"2025-09-15\", 6999.00)\n",
        "insert_receipt(\"Chumbak - Coffee Mug Set\", \"Home Decor\", \"2025-09-16\", 999.00)\n",
        "insert_receipt(\"Fastrack - Sunglasses\", \"Accessories\", \"2025-09-17\", 1799.00)\n",
        "insert_receipt(\"IKEA - Desk Lamp\", \"Home Decor\", \"2025-09-18\", 1290.00)\n"
      ],
      "metadata": {
        "id": "mD2ey655pESy"
      },
      "execution_count": 2,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "from google.colab import files\n",
        "files.download('receipts.db')"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 17
        },
        "id": "ksRBej-2pqwa",
        "outputId": "37ea7f28-2e01-43cb-c024-418e7227d664"
      },
      "execution_count": 3,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<IPython.core.display.Javascript object>"
            ],
            "application/javascript": [
              "\n",
              "    async function download(id, filename, size) {\n",
              "      if (!google.colab.kernel.accessAllowed) {\n",
              "        return;\n",
              "      }\n",
              "      const div = document.createElement('div');\n",
              "      const label = document.createElement('label');\n",
              "      label.textContent = `Downloading \"${filename}\": `;\n",
              "      div.appendChild(label);\n",
              "      const progress = document.createElement('progress');\n",
              "      progress.max = size;\n",
              "      div.appendChild(progress);\n",
              "      document.body.appendChild(div);\n",
              "\n",
              "      const buffers = [];\n",
              "      let downloaded = 0;\n",
              "\n",
              "      const channel = await google.colab.kernel.comms.open(id);\n",
              "      // Send a message to notify the kernel that we're ready.\n",
              "      channel.send({})\n",
              "\n",
              "      for await (const message of channel.messages) {\n",
              "        // Send a message to notify the kernel that we're ready.\n",
              "        channel.send({})\n",
              "        if (message.buffers) {\n",
              "          for (const buffer of message.buffers) {\n",
              "            buffers.push(buffer);\n",
              "            downloaded += buffer.byteLength;\n",
              "            progress.value = downloaded;\n",
              "          }\n",
              "        }\n",
              "      }\n",
              "      const blob = new Blob(buffers, {type: 'application/binary'});\n",
              "      const a = document.createElement('a');\n",
              "      a.href = window.URL.createObjectURL(blob);\n",
              "      a.download = filename;\n",
              "      div.appendChild(a);\n",
              "      a.click();\n",
              "      div.remove();\n",
              "    }\n",
              "  "
            ]
          },
          "metadata": {}
        },
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<IPython.core.display.Javascript object>"
            ],
            "application/javascript": [
              "download(\"download_16579fa7-232c-4f69-84c7-39cfba3686c8\", \"receipts.db\", 12288)"
            ]
          },
          "metadata": {}
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "tg05xFYiPjwe"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}