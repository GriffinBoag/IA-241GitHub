{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "6f00548f",
   "metadata": {},
   "source": [
    "Lab 12. Data Analysis in Python"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "8b0e55cb",
   "metadata": {},
   "source": [
    "load data into pandas.dataframe"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "d561a647",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "1a99d12e",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>ID</th>\n",
       "      <th>price</th>\n",
       "      <th>bedroom</th>\n",
       "      <th>bathroom</th>\n",
       "      <th>house_type</th>\n",
       "      <th>lot_size</th>\n",
       "      <th>built_in</th>\n",
       "      <th>area</th>\n",
       "      <th>days</th>\n",
       "      <th>views</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>993</td>\n",
       "      <td>229900</td>\n",
       "      <td>3</td>\n",
       "      <td>2</td>\n",
       "      <td>single-family home</td>\n",
       "      <td>10018</td>\n",
       "      <td>2002</td>\n",
       "      <td>1541</td>\n",
       "      <td>77</td>\n",
       "      <td>1357</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>994</td>\n",
       "      <td>149900</td>\n",
       "      <td>4</td>\n",
       "      <td>2</td>\n",
       "      <td>single-family home</td>\n",
       "      <td>8712</td>\n",
       "      <td>1975</td>\n",
       "      <td>1810</td>\n",
       "      <td>5</td>\n",
       "      <td>1282</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>995</td>\n",
       "      <td>229900</td>\n",
       "      <td>3</td>\n",
       "      <td>2</td>\n",
       "      <td>single-family home</td>\n",
       "      <td>13504</td>\n",
       "      <td>1988</td>\n",
       "      <td>1456</td>\n",
       "      <td>76</td>\n",
       "      <td>947</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>996</td>\n",
       "      <td>359000</td>\n",
       "      <td>5</td>\n",
       "      <td>4</td>\n",
       "      <td>single-family home</td>\n",
       "      <td>10130</td>\n",
       "      <td>1997</td>\n",
       "      <td>2903</td>\n",
       "      <td>79</td>\n",
       "      <td>951</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>999</td>\n",
       "      <td>394000</td>\n",
       "      <td>3</td>\n",
       "      <td>2</td>\n",
       "      <td>single-family home</td>\n",
       "      <td>18295</td>\n",
       "      <td>2001</td>\n",
       "      <td>2616</td>\n",
       "      <td>73</td>\n",
       "      <td>709</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>1000</td>\n",
       "      <td>349900</td>\n",
       "      <td>3</td>\n",
       "      <td>2</td>\n",
       "      <td>single-family home</td>\n",
       "      <td>204732</td>\n",
       "      <td>1967</td>\n",
       "      <td>3850</td>\n",
       "      <td>42</td>\n",
       "      <td>366</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6</th>\n",
       "      <td>1002</td>\n",
       "      <td>148500</td>\n",
       "      <td>3</td>\n",
       "      <td>1</td>\n",
       "      <td>single-family home</td>\n",
       "      <td>9147</td>\n",
       "      <td>1959</td>\n",
       "      <td>1000</td>\n",
       "      <td>17</td>\n",
       "      <td>328</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>7</th>\n",
       "      <td>1003</td>\n",
       "      <td>134900</td>\n",
       "      <td>2</td>\n",
       "      <td>2</td>\n",
       "      <td>townhouse</td>\n",
       "      <td>2300</td>\n",
       "      <td>1994</td>\n",
       "      <td>920</td>\n",
       "      <td>56</td>\n",
       "      <td>328</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>8</th>\n",
       "      <td>1004</td>\n",
       "      <td>265000</td>\n",
       "      <td>3</td>\n",
       "      <td>3</td>\n",
       "      <td>single-family home</td>\n",
       "      <td>13939</td>\n",
       "      <td>1998</td>\n",
       "      <td>2705</td>\n",
       "      <td>12</td>\n",
       "      <td>362</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>9</th>\n",
       "      <td>1005</td>\n",
       "      <td>149900</td>\n",
       "      <td>4</td>\n",
       "      <td>3</td>\n",
       "      <td>townhouse</td>\n",
       "      <td>2291</td>\n",
       "      <td>1999</td>\n",
       "      <td>1440</td>\n",
       "      <td>4</td>\n",
       "      <td>137</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "     ID   price  bedroom  bathroom          house_type  lot_size  built_in  \\\n",
       "0   993  229900        3         2  single-family home     10018      2002   \n",
       "1   994  149900        4         2  single-family home      8712      1975   \n",
       "2   995  229900        3         2  single-family home     13504      1988   \n",
       "3   996  359000        5         4  single-family home     10130      1997   \n",
       "4   999  394000        3         2  single-family home     18295      2001   \n",
       "5  1000  349900        3         2  single-family home    204732      1967   \n",
       "6  1002  148500        3         1  single-family home      9147      1959   \n",
       "7  1003  134900        2         2           townhouse      2300      1994   \n",
       "8  1004  265000        3         3  single-family home     13939      1998   \n",
       "9  1005  149900        4         3           townhouse      2291      1999   \n",
       "\n",
       "   area  days  views  \n",
       "0  1541    77   1357  \n",
       "1  1810     5   1282  \n",
       "2  1456    76    947  \n",
       "3  2903    79    951  \n",
       "4  2616    73    709  \n",
       "5  3850    42    366  \n",
       "6  1000    17    328  \n",
       "7   920    56    328  \n",
       "8  2705    12    362  \n",
       "9  1440     4    137  "
      ]
     },
     "execution_count": 3,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df = pandas.read_excel('s3://ia241boag/house_price.xls')\n",
    "\n",
    "df[:10]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "a84de8b3",
   "metadata": {
    "collapsed": true,
    "jupyter": {
     "outputs_hidden": true
    }
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>ID</th>\n",
       "      <th>price</th>\n",
       "      <th>bedroom</th>\n",
       "      <th>bathroom</th>\n",
       "      <th>house_type</th>\n",
       "      <th>lot_size</th>\n",
       "      <th>built_in</th>\n",
       "      <th>area</th>\n",
       "      <th>days</th>\n",
       "      <th>views</th>\n",
       "      <th>unit_price</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>993</td>\n",
       "      <td>229900</td>\n",
       "      <td>3</td>\n",
       "      <td>2</td>\n",
       "      <td>single-family home</td>\n",
       "      <td>10018</td>\n",
       "      <td>2002</td>\n",
       "      <td>1541</td>\n",
       "      <td>77</td>\n",
       "      <td>1357</td>\n",
       "      <td>149.188838</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>994</td>\n",
       "      <td>149900</td>\n",
       "      <td>4</td>\n",
       "      <td>2</td>\n",
       "      <td>single-family home</td>\n",
       "      <td>8712</td>\n",
       "      <td>1975</td>\n",
       "      <td>1810</td>\n",
       "      <td>5</td>\n",
       "      <td>1282</td>\n",
       "      <td>82.817680</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>995</td>\n",
       "      <td>229900</td>\n",
       "      <td>3</td>\n",
       "      <td>2</td>\n",
       "      <td>single-family home</td>\n",
       "      <td>13504</td>\n",
       "      <td>1988</td>\n",
       "      <td>1456</td>\n",
       "      <td>76</td>\n",
       "      <td>947</td>\n",
       "      <td>157.898352</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>996</td>\n",
       "      <td>359000</td>\n",
       "      <td>5</td>\n",
       "      <td>4</td>\n",
       "      <td>single-family home</td>\n",
       "      <td>10130</td>\n",
       "      <td>1997</td>\n",
       "      <td>2903</td>\n",
       "      <td>79</td>\n",
       "      <td>951</td>\n",
       "      <td>123.665174</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>999</td>\n",
       "      <td>394000</td>\n",
       "      <td>3</td>\n",
       "      <td>2</td>\n",
       "      <td>single-family home</td>\n",
       "      <td>18295</td>\n",
       "      <td>2001</td>\n",
       "      <td>2616</td>\n",
       "      <td>73</td>\n",
       "      <td>709</td>\n",
       "      <td>150.611621</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>1000</td>\n",
       "      <td>349900</td>\n",
       "      <td>3</td>\n",
       "      <td>2</td>\n",
       "      <td>single-family home</td>\n",
       "      <td>204732</td>\n",
       "      <td>1967</td>\n",
       "      <td>3850</td>\n",
       "      <td>42</td>\n",
       "      <td>366</td>\n",
       "      <td>90.883117</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6</th>\n",
       "      <td>1002</td>\n",
       "      <td>148500</td>\n",
       "      <td>3</td>\n",
       "      <td>1</td>\n",
       "      <td>single-family home</td>\n",
       "      <td>9147</td>\n",
       "      <td>1959</td>\n",
       "      <td>1000</td>\n",
       "      <td>17</td>\n",
       "      <td>328</td>\n",
       "      <td>148.500000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>7</th>\n",
       "      <td>1003</td>\n",
       "      <td>134900</td>\n",
       "      <td>2</td>\n",
       "      <td>2</td>\n",
       "      <td>townhouse</td>\n",
       "      <td>2300</td>\n",
       "      <td>1994</td>\n",
       "      <td>920</td>\n",
       "      <td>56</td>\n",
       "      <td>328</td>\n",
       "      <td>146.630435</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>8</th>\n",
       "      <td>1004</td>\n",
       "      <td>265000</td>\n",
       "      <td>3</td>\n",
       "      <td>3</td>\n",
       "      <td>single-family home</td>\n",
       "      <td>13939</td>\n",
       "      <td>1998</td>\n",
       "      <td>2705</td>\n",
       "      <td>12</td>\n",
       "      <td>362</td>\n",
       "      <td>97.966728</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>9</th>\n",
       "      <td>1005</td>\n",
       "      <td>149900</td>\n",
       "      <td>4</td>\n",
       "      <td>3</td>\n",
       "      <td>townhouse</td>\n",
       "      <td>2291</td>\n",
       "      <td>1999</td>\n",
       "      <td>1440</td>\n",
       "      <td>4</td>\n",
       "      <td>137</td>\n",
       "      <td>104.097222</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "     ID   price  bedroom  bathroom          house_type  lot_size  built_in  \\\n",
       "0   993  229900        3         2  single-family home     10018      2002   \n",
       "1   994  149900        4         2  single-family home      8712      1975   \n",
       "2   995  229900        3         2  single-family home     13504      1988   \n",
       "3   996  359000        5         4  single-family home     10130      1997   \n",
       "4   999  394000        3         2  single-family home     18295      2001   \n",
       "5  1000  349900        3         2  single-family home    204732      1967   \n",
       "6  1002  148500        3         1  single-family home      9147      1959   \n",
       "7  1003  134900        2         2           townhouse      2300      1994   \n",
       "8  1004  265000        3         3  single-family home     13939      1998   \n",
       "9  1005  149900        4         3           townhouse      2291      1999   \n",
       "\n",
       "   area  days  views  unit_price  \n",
       "0  1541    77   1357  149.188838  \n",
       "1  1810     5   1282   82.817680  \n",
       "2  1456    76    947  157.898352  \n",
       "3  2903    79    951  123.665174  \n",
       "4  2616    73    709  150.611621  \n",
       "5  3850    42    366   90.883117  \n",
       "6  1000    17    328  148.500000  \n",
       "7   920    56    328  146.630435  \n",
       "8  2705    12    362   97.966728  \n",
       "9  1440     4    137  104.097222  "
      ]
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df['unit_price']=df['price']/df['area']\n",
    "df[:10]"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "fdc8a69f",
   "metadata": {},
   "source": [
    "##2.2 house type"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "455f3c50",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "single-family home    36\n",
       "townhouse              3\n",
       "condo                  2\n",
       "Name: house_type, dtype: int64"
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df['house_type'].value_counts()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "2f8588ae",
   "metadata": {},
   "source": [
    "##2.3 average price more than two bathrooms"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "4958c850",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "avg price of houses more than 2 bathrooms is $383645.45454545453\n"
     ]
    }
   ],
   "source": [
    "prc_more_2_bath=df.loc[ df['bathroom']>2 ]['price']\n",
    "\n",
    "print('avg price of houses more than 2 bathrooms is ${}'.format(prc_more_2_bath.mean()))"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "a235c390",
   "metadata": {},
   "source": [
    "2.4 mean/median unit price"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "6520995d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "mean unit price is $167.45934522134766\n"
     ]
    }
   ],
   "source": [
    "print('mean unit price is ${}'.format(df['unit_price'].mean()))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "bee04087",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "mean unit price is $130.13392857142858\n"
     ]
    }
   ],
   "source": [
    "print('mean unit price is ${}'.format(df['unit_price'].median()))"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "0bed4409",
   "metadata": {},
   "source": [
    "##2.5 avg price per house type"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "77c81b2e",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "house_type\n",
       "condo                 164450.000000\n",
       "single-family home    378236.111111\n",
       "townhouse             164600.000000\n",
       "Name: price, dtype: float64"
      ]
     },
     "execution_count": 17,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.groupby('house_type').mean()['price']"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "acb8713d",
   "metadata": {},
   "source": [
    "##2.6 predict price by house area"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "90063241",
   "metadata": {},
   "outputs": [],
   "source": [
    "from scipy import stats"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "040b3e12",
   "metadata": {},
   "outputs": [],
   "source": [
    "result = stats.linregress(df['area'],df['price'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "id": "6a620ff4",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "slope is 79.95495729411489\n",
      "slope is 156254.76245096227\n",
      "r square is 0.2343900121890692\n",
      "p value is 0.001340065037461188\n"
     ]
    }
   ],
   "source": [
    "print('slope is {}'.format(result.slope))\n",
    "print('slope is {}'.format(result.intercept))\n",
    "print('r square is {}'.format(result.rvalue *result.rvalue ))\n",
    "print('p value is {}'.format(result.pvalue))"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "2c87b49a",
   "metadata": {},
   "source": [
    "##2.7 predict price of house 2,000 sqft"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "id": "cd1788ec",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "price of a house with 2000 sqft is $316164.67703919206\n"
     ]
    }
   ],
   "source": [
    "print('price of a house with {} sqft is ${}'.format(2000,2000*result.slope+result.intercept))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "ac4cfd52",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "conda_python3",
   "language": "python",
   "name": "conda_python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.6.13"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
