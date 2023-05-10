# Age information into a separate dataframe
age_data = app_train[['TARGET', 'DAYS_BIRTH']]
age_data['YEARS_BIRTH'] = age_data['DAYS_BIRTH'] / 365

# Bin the age data
age_data['YEARS_BINNED'] = pd.cut(age_data['YEARS_BIRTH'], bins = np.linspace(20, 70, num = 11))
age_data.head(10)

"""
np.linspace(20, 70, num=11) ifadesi, 20 ile 70 arasında (dahil) eşit aralıklı 11 değer üretir.
Bu değerler, yaş aralıklarının sınırlarını temsil eder. Örneğin, [20, 25, 30, 35, ..., 65, 70]
gibi bir dizi oluşturulur.

    pd.cut() fonksiyonu, veri kümesindeki belirli bir sütunu (bu durumda YEARS_BIRTH) ve belirli aralıkları (bu durumda bins) kullanarak kesitlere ayırır.

    age_data['YEARS_BIRTH'] ifadesi, age_data veri kümesindeki YEARS_BIRTH sütununa erişim sağlar.

    bins parametresine önceden belirlenmiş aralıklar (yaş kesitleri) verilir. Bu aralıklar, yaş değerlerinin sınıflandırılacağı aralıkları temsil eder.

"""
