# RAGAS Test Data

File ini digenerate dari tabel `chats`, `chat_references`, dan `document_chunks`.
`retrieved_context` memakai `document_chunks.content` jika tersedia, lalu fallback ke `chat_references.quote`.
`reference` sengaja dikosongkan agar dapat diisi manual.

## Sample 6

- conversation_id: 14
- user_chat_id: 676
- bot_chat_id: 677

### user_input

Bagaimana software engineering menggunakan software metrics?

### retrieved_context

1. Measurement is needed to validate the effectiveness of software development process. The phrase software metrics describes measurements made on an artifact of software whereas a software artifact has two significant elements: the coded implementation, and the document of its design specification. The initially calculated McCabe, Halstead, and Albrecht metrics, presented during the 1970s, were typically constructed on the coded final software products. Examples of software science metrics include [1] function point analysis [2], and cyclomatic complexity metric [3], which predominated in the early 1980s to measure software product. (Efficacy of Inheritance Aspect in Software Fault Prediction—A Survey Paper, page 1)

2. Software metrics make it easy for developers to audit and monitor the quality of software design as the project progresses. In addition, predicting the probability of defective classes is needed to help the software engineers during development to enhance the quality of software and reduce testing and maintenance costs. For example, in order to increase the productivity of software testing, software evaluators can plan tests based on the parts most prone to faults.

TABLE 1. List of inheritance metrics.

Software metrics and fault data for an earlier software version are utilized to make an SFP model for the next software version [83]. When a software has faults, it leades to a disaster because it has a significant human dependency on it. Therefore, there is an emerging requirement for software without faults. Software Companies are expanding to discover faults in software. Producing software without faults is a challenging job. To lower costs and improve software usefulness, it is vital to classify classes which are faulty. Many software metrics are proposed by the researchers to gauge the software quality. In object-oriented paradigm, metrics are beneficial for software engineers to make additional information associated with software quality available. Quality of software can also be monitored through metrics, while software evaluators use metrics to increase the effectiveness of testing [84]. (Experimental Validation of Inheritance Metrics’ Impact on Software Fault Prediction, page 3)

3. Metrics and roles play a fundamental role in SD, as supported by GAI. The utilization of these metrics enables the establishment of an objective for evaluating the quality of AI-generated codes, including their accuracy and efficiency. These measures empower developers to evaluate the congruence between the resulting artifacts and original objectives, thereby identifying opportunities for enhancement [21], [22]. More broadly, metrics support software engineering quality assessment by quantifying the key characteristics of the development process, including efficiency and maintainability. A review of the literature reveals that commonly reported metrics include structural complexity measures, which assess software architecture using indicators such as the number of modules and interconnections [23]. Quality metrics are used to forecast software reliability and support decision-making throughout the SDLC [24]. Finally, productivity metrics are reported, and these assess the impact of GAI-based tools on development speed, quality, and overall efficiency [6], [25]. (Generative Artificial Intelligence for Software Development Using ISO/IEC 29110 Basic Profile: Gaps and Opportunities, page 2)

4. Metrics and roles play a fundamental role in SD, as supported by GAI. The utilization of these metrics enables the establishment of an objective for evaluating the quality of AI-generated codes, including their accuracy and efficiency. These measures empower developers to evaluate the congruence between the resulting artifacts and original objectives, thereby identifying opportunities for enhancement [21], [22]. More broadly, metrics support software engineering quality assessment by quantifying the key characteristics of the development process, including efficiency and maintainability. A review of the literature reveals that commonly reported metrics include structural complexity measures, which assess software architecture using indicators such as the number of modules and interconnections [23]. Quality metrics are used to forecast software reliability and support decision-making throughout the SDLC [24]. Finally, productivity metrics are reported, and these assess the impact of GAI-based tools on development speed, quality, and overall efficiency [6], [25]. (Generative Artificial Intelligence for Software Development Using ISO/IEC 29110 Basic Profile: Gaps and Opportunities, page 2)

5. Software metrics are foundation to quantify complexity, quality of software, and project costs with effort estimation. Function points and cyclomatic complexity are traditional metrics. These are being utilized in the paradigm of procedure language. Nonetheless, these may not merely be utilized in the context of object-oriented [21]. The procedural languages are less complex while comparing with object-oriented programming language [22]. The majority of studies specified hurdles in moving from a procedural approach towards an objectoriented paradigm [23].In object-oriented, it is problematic to comprehend how inheritance, abstraction, and encapsulation associated with each other. (Efficacy of Inheritance Aspect in Software Fault Prediction—A Survey Paper, page 1)

6. TABLE 2. Frequently Used Metrics in Software Fault Prediction.

Tabel ini memuat beberapa studi terkait penggunaan metrik dalam prediksi kegagalan perangkat lunak. Lima belas penelitian yang disebutkan menunjukkan bahwa beberapa metrik telah digunakan secara luas dalam prediksi kegagalan, seperti metrik yang terkait dengan sifat objek-oriented dan perilaku pengguna.

Variabel utama di tabel ini meliputi nama penulis, judul penelitian, metode yang digunakan, serta hasil yang diperoleh. Nilai penting dari tabel ini adalah penemuan bahwa beberapa metrik khususnya terkait dengan sifat objek-oriented telah terbukti efektif dalam prediksi kegagalan perangkat lunak.

Pola penting dapat dilihat dari kemunculan istilah-istilah seperti "C&K metrics" dan "Li and Henry," yang mengindikasikan bahwa ada metrik yang secara konsisten digunakan dalam penelitian-penelitian ini. Selain itu, juga terlihat bahwa beberapa penulis menggunakan kombinasi berbagai metode analisis untuk mencapai hasil prediksi yang lebih akurat.

Insight singkat dari tabel ini adalah pentingnya penggunaan metrik-metrik tertentu dalam prediksi kegagalan perangkat lunak. Dengan demikian, penelitian ini menunjukkan bahwa dengan memahami dan menggunakan metrik yang tepat, kita dapat meningkatkan akurasi prediksi kegagalan perangkat lunak. (Efficacy of Inheritance Aspect in Software Fault Prediction—A Survey Paper, page 13)

7. TABLE 2. Class-level software metric used in this study.

Tabel ini memuat beberapa metrik kelas untuk prediksi kesalahan perangkat lunak. Data tabel menunjukkan bahwa ada dua dataset utama: Software Metrics dan Full Dataset. Kedua dataset tersebut berbeda dalam hal variabel independen yang digunakan, yaitu ESM (Error-Severity Metric) values dan software metrics yang diekstraksi dari modul perangkat lunak.

Pada tabel ini, kita dapat melihat bahwa terdapat tiga jenis metrik ESM: IndexOutOfBounds, NullPointer, dan ClassCast. Masing-masing metrik tersebut memiliki nilai-nilai yang berbeda-beda pada kedua dataset. Pada Software Metrics Dataset, variabel independen hanya mencakup software metrics, sedangkan pada Full Dataset juga termasuk ESM values.

Dengan memperhatikan tabel ini, kita dapat menyimpulkan bahwa peneliti menggunakan metrik-metrik tersebut untuk memprediksi kesalahan perangkat lunak. Pada dataset yang lebih lengkap (Full Dataset), penulis juga melibatkan ESM values sebagai variabel independen tambahan. Hal ini menunjukkan bahwa penulis ingin mengetahui bagaimana pengaruh nilai-nilai ESM terhadap performa model pelatihan machine learning.

Dalam konteks yang lebih luas, tabel ini memberikan gambaran tentang cara peneliti menggunakan metrik kelas untuk prediksi kesalahan perangkat lunak. Penemuan penulis dapat berguna dalam meningkatkan akurasi model pemodelan perangkat lunak dan mengidentifikasi potensi masalah yang mungkin terjadi pada sistem. (Error-Type—A Novel Set of Software Metrics for Software Fault Prediction, page 6)

8. The software metrics are the basis to measure the complexity, quality of software and estimate cost along with efforts of projects. Traditional metrics such as function point and cyclomatic complexity have been employed in the procedure paradigm. But, these are not simply used in object-oriented paradigm [39], [40]. Object Oriented programming is complex while comparing it with procedural languages [41]. Most studies stated difficulty in switching to the object-oriented paradigm from the procedural approach [42]. In Objectoriented Programming, it is difficult to understand how features, for example abstraction, inheritance and encapsulation relate to each other [43]. (Experimental Validation of Inheritance Metrics’ Impact on Software Fault Prediction, page 1)

### response

Software engineering menggunakan software metrics untuk mengevaluasi kualitas dan kompleksitas perangkat lunak, serta memperkirakan biaya dan upaya proyek. Metrik tradisional seperti fungsi poin dan kompleksitas siklokompleks telah digunakan dalam paradigma prosedur. Namun, metrik-metrik ini tidak dapat secara langsung digunakan pada paradigma berorientasi objek (object-oriented).

### reference


Measurement is needed to validate the effectiveness of software development process. The phrase software metrics describes measurements made on an artifact of software whereas a software artifact has two significant elements: the coded implementation, and the document of its design specification.

Software metrics make it easy for developers to audit and monitor the quality of software design as the project progresses. In addition, predicting the probability of defective classes is needed to help the software engineers during development to enhance the quality of software and reduce testing and maintenance costs.

Metrics and roles play a fundamental role in SD, as supported by GAI. The utilization of these metrics enables the establishment of an objective for evaluating the quality of AI-generated codes, including their accuracy and efficiency.

Software metrics are foundation to quantify complexity, quality of software, and project costs with effort estimation. Function points and cyclomatic complexity are traditional metrics.

Frequently Used Metrics in Software Fault Prediction. Tabel ini memuat beberapa studi terkait penggunaan metrik dalam prediksi kegagalan perangkat lunak.

Class-level software metric used in this study. Tabel ini memuat beberapa metrik kelas untuk prediksi kesalahan perangkat lunak.

The software metrics are the basis to measure the complexity, quality of software and estimate cost along with efforts of projects. Traditional metrics such as function point and cyclomatic complexity have been employed in the procedure paradigm.

---

## Sample 7

- conversation_id: 14
- user_chat_id: 678
- bot_chat_id: 679

### user_input

Apa itu software quality?

### retrieved_context

1. Quality is defined by ISO 8042 [18] as ''the totality of characteristics of an entity that bear on its ability to satisfy stated and implied needs''. This definition is too abstract to be operationalized directly, and is one of the reasons why there has been a multitude of software QMs proposed in the last four decades (e.g., [15], [19]- [22]) that refine high-level concepts of ''quality'' (like reliability or efficiency) down to the level of metrics (as number of bugs or response time). One popular example widely adopted in industry is the ISO/IEC 25010 standard [14], which determines the quality aspects to be taken into account when evaluating the properties of a software product. Two more recent examples well known in industry are Quamoco and SQALE [23]. Quamoco [16] is a QM integrating abstract quality aspects and concrete quality measurements. SQALE [24] computes technical debt indexes based on the violations of quality rules in the source code. Other works propose refactoring models to improve a particular quality aspect of the existing model or code, and different extensions to the traditional concept of quality (such as incorporation of non-technical criteria into ISO/IEC 9126-1 QM [25]). (Continuously Assessing and Improving Software Quality With Software Analytics Tools: A Case Study, page 1)

2. Quality is defined by ISO 8042 [18] as ''the totality of characteristics of an entity that bear on its ability to satisfy stated and implied needs''. This definition is too abstract to be operationalized directly, and is one of the reasons why there has been a multitude of software QMs proposed in the last four decades (e.g., [15], [19]- [22]) that refine high-level concepts of ''quality'' (like reliability or efficiency) down to the level of metrics (as number of bugs or response time). One popular example widely adopted in industry is the ISO/IEC 25010 standard [14], which determines the quality aspects to be taken into account when evaluating the properties of a software product. Two more recent examples well known in industry are Quamoco and SQALE [23]. Quamoco [16] is a QM integrating abstract quality aspects and concrete quality measurements. SQALE [24] computes technical debt indexes based on the violations of quality rules in the source code. Other works propose refactoring models to improve a particular quality aspect of the existing model or code, and different extensions to the traditional concept of quality (such as incorporation of non-technical criteria into ISO/IEC 9126-1 QM [25]). (Continuously Assessing and Improving Software Quality With Software Analytics Tools: A Case Study, page 1)

3. Software quality is defined by how closely a software system meets a desired combination of quality attributes [6], [7]. These attributes include complexity, reliability, scalability, functionality, efficiency, portability, usability, and maintainability, each contributing to the system's overall effectiveness [8], [9]. These quality attributes reflect the actual characteristics of the implemented system [8].

In AI-based systems, quality attributes are critical in shaping architectural decisions [4]. These systems introduce additional challenges, such as model management, accuracy, robustness, and inference latency [3], which the architectural design process must carefully address. Consequently, selecting an appropriate architectural style ensures that AI-based software systems meet their requirements effectively. (Architectural Styles and Quality Attributes in AI-Based Video Software: A Systematic Literature Review, page 1)

4. In order to effectively coordinate and evaluate software quality management efforts, software companies use software quality models [34], [37], [44], [45]. The earliest software quality model was proposed by McCall in 1976. The McCall model was later revised by Boehm and Dromey [41], [44], [46], [47]. Recently developed software quality evaluation models include ISO/IEC 25010 which outlines 8 attributes to be used for software quality assessment. In contrast, the earlier version ISO/IEC 9126 adopts 6 characteristics [44], [45], [48].

Despite being viewed as a useful tool for quality assurance [44], software standards or models lack functionality and practical application owing to the ambiguity involved [37], [47]. Gorla and Lin as cited in [49] propose a software quality assessment model that includes relevance and usefulness (i.e., functionality), usability, maintainability, and reliability attributes. On the other hand, other scholars identify usability, reliability, functionality, performance efficiency, portability, and maintainability as important quality measurements [40], [46]. Similarly, several studies identify functionality, usability, reliability, performance efficiency, and maintainability as the most impactful measures of software quality [14], [41], [43], [45]. Consequently, functionality, usability, performance efficiency, reliability, and maintainability indicators are adopted for the evaluation of software quality in this study. (How Software Quality Mediates the Impact of Intellectual Capital on Commercial Open-Source Software Company Success, page 1)

5. In general, quality is considered as the most vital factor for meeting customer expectations and organizational growth [12], [34], [40]. More specifically, software quality is a critical success factor for software development companies [12], [13], [41]. Software development companies often depend on effective coordination of software development processes and quality management activities (engineering) to attain the desired level of software quality. In addition to effective coordination, software quality is also affected by cost and time constraints [12], [13], [42], [43]. (How Software Quality Mediates the Impact of Intellectual Capital on Commercial Open-Source Software Company Success, page 3)

6. Software quality is the total characteristics of an entity that depends on its capacity to satisfy explicit and implicit VOLUME 10, 2022 needs [34]- [36]. Hence, poor software quality negatively impacts not only customer satisfaction but also software maintainability, economic gains, and human life in the real-world context [12], [34], [37], [38]. Software maintenance is the most expensive activity in the software development process, representing about 75% of the total cost. Investing in maintenance and defect prevention efforts is critical because software defects have a detrimental effect on the proper functioning of the software. For instance, the world economy has lost 1.1 trillion dollars in 2016 because of software defects, and an estimated 4.4 billion people were affected [38]. A recent report by the Consortium for Information and Software Quality puts the total financial damage caused by poor quality software at 2.08 trillion dollars in 2020 in the US alone [39]. (How Software Quality Mediates the Impact of Intellectual Capital on Commercial Open-Source Software Company Success, page 2)

7. Software quality is calculated in the following formula (4):  In formula (4), q is Software quality; b is Open bugs; l is Total changed codes. Software quality is expressed by the bug rate, which is equal to the number of Open bugs divided by the Total changed codes.

In Quality assurance subsystem, Code review by numerous reviewers, particularly when carried out in tandem with automatic test, can significantly, positively impact software quality. Code review in Figure 7 is a ratio of the effectiveness of the review. If it is equal to 0, it means that the changed code is not reviewed. In the following empirical case study (in Section III), we input a random function to analyze its impact. (Change-Oriented Open Source Software Process Simulation, page 1)

8. TABLE 4. Path coefficients.

Analisis terbaru mengenai komponen kualitas perangkat lunak (software quality) dalam menengahi dampak modal intelektual (intellectual capital) pada kesuksesan perusahaan swasta open-source software (COSS) telah membawa beberapa temuan penting. Data yang dianalisis menunjukkan bahwa ada hubungan positif signifikan antara kualitas perangkat lunak dan kesuksesan COSS (β = 0,581, T-value = 10,842, P-value = 0,000). Sebenarnya, kualitas perangkat lunak memainkan peran mediasi yang signifikan dalam menengahi hubungan antara modal intelektual dan kesuksesan COSS.

Penelitian ini juga menemukan bahwa ada hubungan positif antara kapital struktural (structural capital) dan kualitas perangkat lunak, serta antara kapital manusia (human capital) dan kualitas perangkat lunak. Dalam beberapa kasus, mediasi efektif kapital manusia pada relasi tersebut terbukti signifikan.

Kemudian, hasil analisis menunjukkan bahwa kualitas perangkat lunak merupakan faktor yang sangat penting dalam mempengaruhi kesuksesan COSS. Dengan demikian, penelitian ini mendukung asumsi-asumsi yang telah diusulkan (H1-H11) mengenai hubungan antara modal intelektual dan kualitas perangkat lunak terhadap kesuksesan COSS.

Dari hasil analisis, dapat disimpulkan bahwa kualitas perangkat lunak merupakan faktor penting dalam menengahi dampak kapital manusia terhadap kesuksesan COSS. Hasil ini dapat dijadikan sebagai rujukan bagi pihak manajemen dan strategis dalam mengembangkan kebijakan yang lebih efektif untuk meningkatkan kinerja perusahaan open-source software mereka. (How Software Quality Mediates the Impact of Intellectual Capital on Commercial Open-Source Software Company Success, page 7)

### response

Software quality adalah totalitas karakteristik suatu entitas yang terkait dengan kemampuannya untuk memenuhi kebutuhan yang telah disatakan dan implisit. (ISO 8042 [18], Source: Continuously Assessing and Improving Software Quality With Software Analytics Tools: A Case Study)

### reference


Quality is defined by ISO 8042 [18] as ''the totality of characteristics of an entity that bear on its ability to satisfy stated and implied needs''.

Software quality is defined by how closely a software system meets a desired combination of quality attributes [6], [7]. These attributes include complexity, reliability, scalability, functionality, efficiency, portability, usability, and maintainability, each contributing to the system's overall effectiveness [8], [9].

In order to effectively coordinate and evaluate software quality management efforts, software companies use software quality models [34], [37], [44], [45]. The earliest software quality model was proposed by McCall in 1976.

In general, quality is considered as the most vital factor for meeting customer expectations and organizational growth [12], [34], [40]. More specifically, software quality is a critical success factor for software development companies [12], [13], [41].

Software quality is the total characteristics of an entity that depends on its capacity to satisfy explicit and implicit VOLUME 10, 2022 needs [34]- [36]. Hence, poor software quality negatively impacts not only customer satisfaction but also software maintainability, economic gains, and human life in the real-world context [12], [34], [37], [38].

Software quality is calculated in the following formula (4): In formula (4), q is Software quality; b is Open bugs; l is Total changed codes. Software quality is expressed by the bug rate, which is equal to the number of Open bugs divided by the Total changed codes.

TABLE 4. Path coefficients.

---

## Sample 8

- conversation_id: 14
- user_chat_id: 680
- bot_chat_id: 681

### user_input

Apa faktor yang mempengaruhi software quality?

### retrieved_context

1. In general, quality is considered as the most vital factor for meeting customer expectations and organizational growth [12], [34], [40]. More specifically, software quality is a critical success factor for software development companies [12], [13], [41]. Software development companies often depend on effective coordination of software development processes and quality management activities (engineering) to attain the desired level of software quality. In addition to effective coordination, software quality is also affected by cost and time constraints [12], [13], [42], [43]. (How Software Quality Mediates the Impact of Intellectual Capital on Commercial Open-Source Software Company Success, page 3)

2. Software quality is the total characteristics of an entity that depends on its capacity to satisfy explicit and implicit VOLUME 10, 2022 needs [34]- [36]. Hence, poor software quality negatively impacts not only customer satisfaction but also software maintainability, economic gains, and human life in the real-world context [12], [34], [37], [38]. Software maintenance is the most expensive activity in the software development process, representing about 75% of the total cost. Investing in maintenance and defect prevention efforts is critical because software defects have a detrimental effect on the proper functioning of the software. For instance, the world economy has lost 1.1 trillion dollars in 2016 because of software defects, and an estimated 4.4 billion people were affected [38]. A recent report by the Consortium for Information and Software Quality puts the total financial damage caused by poor quality software at 2.08 trillion dollars in 2020 in the US alone [39]. (How Software Quality Mediates the Impact of Intellectual Capital on Commercial Open-Source Software Company Success, page 2)

3. The quality of software continues to be a significant challenge in the software industry, and this challenge is more visible in the Small Software Companies (SSCs) to the extent that up to 70 percent of software projects are challenged either due to defects, cost overruns or overshot scheduling related challenges [1]. Although the products produced by the SSCs fail to meet the expected quality, software is still central in influencing human activity. Recent studies indicate that most aspects of society depend on software; moreover, SSCs are responsible for up to 80 percent of software produced on the market. The contribution of SSCs cannot be underestimated since they represent up to 90 percent of software companies in the industry [2]. (Theory on Non-Technical Characteristics Affecting Process Adoption in Small Software Companies: A Grounded Theory Study, page 1)

4. Software quality is defined by how closely a software system meets a desired combination of quality attributes [6], [7]. These attributes include complexity, reliability, scalability, functionality, efficiency, portability, usability, and maintainability, each contributing to the system's overall effectiveness [8], [9]. These quality attributes reflect the actual characteristics of the implemented system [8].

In AI-based systems, quality attributes are critical in shaping architectural decisions [4]. These systems introduce additional challenges, such as model management, accuracy, robustness, and inference latency [3], which the architectural design process must carefully address. Consequently, selecting an appropriate architectural style ensures that AI-based software systems meet their requirements effectively. (Architectural Styles and Quality Attributes in AI-Based Video Software: A Systematic Literature Review, page 1)

5. TABLE 4. Path coefficients.

Analisis terbaru mengenai komponen kualitas perangkat lunak (software quality) dalam menengahi dampak modal intelektual (intellectual capital) pada kesuksesan perusahaan swasta open-source software (COSS) telah membawa beberapa temuan penting. Data yang dianalisis menunjukkan bahwa ada hubungan positif signifikan antara kualitas perangkat lunak dan kesuksesan COSS (β = 0,581, T-value = 10,842, P-value = 0,000). Sebenarnya, kualitas perangkat lunak memainkan peran mediasi yang signifikan dalam menengahi hubungan antara modal intelektual dan kesuksesan COSS.

Penelitian ini juga menemukan bahwa ada hubungan positif antara kapital struktural (structural capital) dan kualitas perangkat lunak, serta antara kapital manusia (human capital) dan kualitas perangkat lunak. Dalam beberapa kasus, mediasi efektif kapital manusia pada relasi tersebut terbukti signifikan.

Kemudian, hasil analisis menunjukkan bahwa kualitas perangkat lunak merupakan faktor yang sangat penting dalam mempengaruhi kesuksesan COSS. Dengan demikian, penelitian ini mendukung asumsi-asumsi yang telah diusulkan (H1-H11) mengenai hubungan antara modal intelektual dan kualitas perangkat lunak terhadap kesuksesan COSS.

Dari hasil analisis, dapat disimpulkan bahwa kualitas perangkat lunak merupakan faktor penting dalam menengahi dampak kapital manusia terhadap kesuksesan COSS. Hasil ini dapat dijadikan sebagai rujukan bagi pihak manajemen dan strategis dalam mengembangkan kebijakan yang lebih efektif untuk meningkatkan kinerja perusahaan open-source software mereka. (How Software Quality Mediates the Impact of Intellectual Capital on Commercial Open-Source Software Company Success, page 7)

6. In order to effectively coordinate and evaluate software quality management efforts, software companies use software quality models [34], [37], [44], [45]. The earliest software quality model was proposed by McCall in 1976. The McCall model was later revised by Boehm and Dromey [41], [44], [46], [47]. Recently developed software quality evaluation models include ISO/IEC 25010 which outlines 8 attributes to be used for software quality assessment. In contrast, the earlier version ISO/IEC 9126 adopts 6 characteristics [44], [45], [48].

Despite being viewed as a useful tool for quality assurance [44], software standards or models lack functionality and practical application owing to the ambiguity involved [37], [47]. Gorla and Lin as cited in [49] propose a software quality assessment model that includes relevance and usefulness (i.e., functionality), usability, maintainability, and reliability attributes. On the other hand, other scholars identify usability, reliability, functionality, performance efficiency, portability, and maintainability as important quality measurements [40], [46]. Similarly, several studies identify functionality, usability, reliability, performance efficiency, and maintainability as the most impactful measures of software quality [14], [41], [43], [45]. Consequently, functionality, usability, performance efficiency, reliability, and maintainability indicators are adopted for the evaluation of software quality in this study. (How Software Quality Mediates the Impact of Intellectual Capital on Commercial Open-Source Software Company Success, page 1)

7. TABLE 1. Size Categories of the Software Systems.

Dalam penelitian ini, beberapa penulis telah mengeksplorasi penggunaan teknik refactoring untuk meningkatkan kualitas sistem perangkat lunak. Variabel utama dalam penelitian ini adalah penggunaan teknik refactoring yang berbeda-beda. Penulis menggunakan model-model Machine Learning (ML) seperti Random Forests, Support Vector Machine (SVM), dan Gaussian Naïve Bayes untuk memprediksi kesempatan menggunakan teknik refactoring.

Penelitian menunjukkan bahwa teknik refactoring dapat meningkatkan kualitas sistem perangkat lunak. Namun, hasil penelitian juga mengungkapkan bahwa beberapa faktor dapat mempengaruhi efektivitas penggunaan teknik refactoring, seperti ukuran proyek dan jenis atribut yang digunakan.

Dalam penelitian ini, ada empat variabel utama yang diamati, yaitu:

* Penggunaan Random Forests (RF) sebagai model prediksi yang paling efektif.
* Efektifitas penggunaan teknik refactoring pada proyek-proyek dengan ukuran besar.
* Faktor-faktor yang mempengaruhi efektivitas penggunaan teknik refactoring, seperti jenis atribut dan ukuran proyek.

Dari hasil penelitian ini dapat disimpulkan bahwa penggunaan teknik refactoring dapat meningkatkan kualitas sistem perangkat lunak, namun perlu dipertimbangkan beberapa faktor yang mempengaruhi efektivitasnya. (Revisiting Scenarios of Using Refactoring Techniques to Improve Software Systems Quality, page 3)

8. A bug in a software program is a failure or fault that prevents the program from running as intended, for example, generating an incorrect result. A software fault is a defect that causes a software failure at runtime. A strategy is needed to predict faults earlier, as it helps to reduce faults and improve the quality of software. The essential part of software development is to ensure that developed software has enhanced quality. It is a well-proven fact that the sooner a fault is detected, the sooner it is resolved, the lesser it costs [1]. (Experimental Validation of Inheritance Metrics’ Impact on Software Fault Prediction, page 1)

### response

Faktor-faktor yang mempengaruhi software quality adalah:

* Ukuran proyek
* Jenis atribut yang digunakan
* Faktor-faktor lainnya seperti kapital struktural dan kapital manusia.

Informasi tersebut ditemukan pada tabel 1 dalam penelitian "Revisiting Scenarios of Using Refactoring Techniques to Improve Software Systems Quality" dan pada analisis terbaru mengenai komponen kualitas perangkat lunak (software quality) dalam menengahi dampak modal intelektual (intellectual capital) pada kesuksesan perusahaan swasta open-source software (COSS).

### reference


In general, quality is considered as the most vital factor for meeting customer expectations and organizational growth [12], [34], [40]. More specifically, software quality is a critical success factor for software development companies [12], [13], [41].

Software quality is the total characteristics of an entity that depends on its capacity to satisfy explicit and implicit VOLUME 10, 2022 needs [34]- [36]. Hence, poor software quality negatively impacts not only customer satisfaction but also software maintainability, economic gains, and human life in the real-world context [12], [34], [37], [38].

The quality of software continues to be a significant challenge in the software industry, and this challenge is more visible in the Small Software Companies (SSCs) to the extent that up to 70 percent of software projects are challenged either due to defects, cost overruns or overshot scheduling related challenges [1].

Software quality is defined by how closely a software system meets a desired combination of quality attributes [6], [7]. These attributes include complexity, reliability, scalability, functionality, efficiency, portability, usability, and maintainability, each contributing to the system's overall effectiveness [8], [9].

TABLE 4. Path coefficients.

In order to effectively coordinate and evaluate software quality management efforts, software companies use software quality models [34], [37], [44], [45]. The earliest software quality model was proposed by McCall in 1976.

Size Categories of the Software Systems. Dalam penelitian ini, beberapa penulis telah mengeksplorasi penggunaan teknik refactoring untuk meningkatkan kualitas sistem perangkat lunak.

A bug in a software program is a failure or fault that prevents the program from running as intended, for example, generating an incorrect result. A software fault is a defect that causes a software failure at runtime.

---

## Sample 9

- conversation_id: 14
- user_chat_id: 682
- bot_chat_id: 683

### user_input

Bagaimana software quality diukur?

### retrieved_context

1. In order to effectively coordinate and evaluate software quality management efforts, software companies use software quality models [34], [37], [44], [45]. The earliest software quality model was proposed by McCall in 1976. The McCall model was later revised by Boehm and Dromey [41], [44], [46], [47]. Recently developed software quality evaluation models include ISO/IEC 25010 which outlines 8 attributes to be used for software quality assessment. In contrast, the earlier version ISO/IEC 9126 adopts 6 characteristics [44], [45], [48].

Despite being viewed as a useful tool for quality assurance [44], software standards or models lack functionality and practical application owing to the ambiguity involved [37], [47]. Gorla and Lin as cited in [49] propose a software quality assessment model that includes relevance and usefulness (i.e., functionality), usability, maintainability, and reliability attributes. On the other hand, other scholars identify usability, reliability, functionality, performance efficiency, portability, and maintainability as important quality measurements [40], [46]. Similarly, several studies identify functionality, usability, reliability, performance efficiency, and maintainability as the most impactful measures of software quality [14], [41], [43], [45]. Consequently, functionality, usability, performance efficiency, reliability, and maintainability indicators are adopted for the evaluation of software quality in this study. (How Software Quality Mediates the Impact of Intellectual Capital on Commercial Open-Source Software Company Success, page 1)

2. Software quality is calculated in the following formula (4):  In formula (4), q is Software quality; b is Open bugs; l is Total changed codes. Software quality is expressed by the bug rate, which is equal to the number of Open bugs divided by the Total changed codes.

In Quality assurance subsystem, Code review by numerous reviewers, particularly when carried out in tandem with automatic test, can significantly, positively impact software quality. Code review in Figure 7 is a ratio of the effectiveness of the review. If it is equal to 0, it means that the changed code is not reviewed. In the following empirical case study (in Section III), we input a random function to analyze its impact. (Change-Oriented Open Source Software Process Simulation, page 1)

3. Software quality is defined by how closely a software system meets a desired combination of quality attributes [6], [7]. These attributes include complexity, reliability, scalability, functionality, efficiency, portability, usability, and maintainability, each contributing to the system's overall effectiveness [8], [9]. These quality attributes reflect the actual characteristics of the implemented system [8].

In AI-based systems, quality attributes are critical in shaping architectural decisions [4]. These systems introduce additional challenges, such as model management, accuracy, robustness, and inference latency [3], which the architectural design process must carefully address. Consequently, selecting an appropriate architectural style ensures that AI-based software systems meet their requirements effectively. (Architectural Styles and Quality Attributes in AI-Based Video Software: A Systematic Literature Review, page 1)

4. Quality is defined by ISO 8042 [18] as ''the totality of characteristics of an entity that bear on its ability to satisfy stated and implied needs''. This definition is too abstract to be operationalized directly, and is one of the reasons why there has been a multitude of software QMs proposed in the last four decades (e.g., [15], [19]- [22]) that refine high-level concepts of ''quality'' (like reliability or efficiency) down to the level of metrics (as number of bugs or response time). One popular example widely adopted in industry is the ISO/IEC 25010 standard [14], which determines the quality aspects to be taken into account when evaluating the properties of a software product. Two more recent examples well known in industry are Quamoco and SQALE [23]. Quamoco [16] is a QM integrating abstract quality aspects and concrete quality measurements. SQALE [24] computes technical debt indexes based on the violations of quality rules in the source code. Other works propose refactoring models to improve a particular quality aspect of the existing model or code, and different extensions to the traditional concept of quality (such as incorporation of non-technical criteria into ISO/IEC 9126-1 QM [25]). (Continuously Assessing and Improving Software Quality With Software Analytics Tools: A Case Study, page 1)

5. Quality is defined by ISO 8042 [18] as ''the totality of characteristics of an entity that bear on its ability to satisfy stated and implied needs''. This definition is too abstract to be operationalized directly, and is one of the reasons why there has been a multitude of software QMs proposed in the last four decades (e.g., [15], [19]- [22]) that refine high-level concepts of ''quality'' (like reliability or efficiency) down to the level of metrics (as number of bugs or response time). One popular example widely adopted in industry is the ISO/IEC 25010 standard [14], which determines the quality aspects to be taken into account when evaluating the properties of a software product. Two more recent examples well known in industry are Quamoco and SQALE [23]. Quamoco [16] is a QM integrating abstract quality aspects and concrete quality measurements. SQALE [24] computes technical debt indexes based on the violations of quality rules in the source code. Other works propose refactoring models to improve a particular quality aspect of the existing model or code, and different extensions to the traditional concept of quality (such as incorporation of non-technical criteria into ISO/IEC 9126-1 QM [25]). (Continuously Assessing and Improving Software Quality With Software Analytics Tools: A Case Study, page 1)

6. Among the ten studies (7.2%) that discussed software quality attributes, the most frequently mentioned were efficiency, complexity, robustness, performance, and scalability. Efficiency was the most commonly reported attribute, appearing in four studies [37], [38], [39], [40], followed by complexity, referenced in three studies [41], [42], [43], while robustness [43], [44], performance [45], and scalability [36] were each mentioned in one or two studies. These studies measured the attributes in different ways across studies. Performance was assessed based on training time, measured in hours per epoch. They evaluated efficiency using response time, computational time, and average response time with prediction rate. Complexity was determined by analyzing the number of parameters in the system. They examined scalability through dataset transfer time to cloud storage and execution time variations under different dataset sizes and processing nodes. Finally, the studies evaluated robustness by measuring prediction accuracy and AUC under various noise conditions. Multiple studies used time cost-the average time required to process a single sample-as a measure of efficiency. Table 4 summarizes the identified quality attributes and their corresponding measurement methods to provide a (Architectural Styles and Quality Attributes in AI-Based Video Software: A Systematic Literature Review, page 1)

7. In general, quality is considered as the most vital factor for meeting customer expectations and organizational growth [12], [34], [40]. More specifically, software quality is a critical success factor for software development companies [12], [13], [41]. Software development companies often depend on effective coordination of software development processes and quality management activities (engineering) to attain the desired level of software quality. In addition to effective coordination, software quality is also affected by cost and time constraints [12], [13], [42], [43]. (How Software Quality Mediates the Impact of Intellectual Capital on Commercial Open-Source Software Company Success, page 3)

8. The faults are not uniformly dispersed within the software components. Some classes have a relatively high number of faults as compare to others and are clustered in a limited number of classes [6]. Source code quality is measured through internal metrics whereas the behavior or functionality of the software is measured by external metrics [4]. In general, these two types of metrics are utilized to assess the quality of the software to indicate the degree of reliability of the software. Presently in software engineering, numerous prediction approaches are being used in the research that includes prediction of reuse, prediction of testing effort, prediction of cost, prediction of security, prediction of faults, prediction of quality, and prediction of stress [7]. Out of these, software fault prediction is an emergent research domain where defective classes are identified during the initial phases of development project [8] by utilizing machine learning [9]. Many approaches make use of typical methods of machine learning, which consist of Support Vector Machines (SVM), Naive Bayes (NB) [10], Decision Trees [11], and Neural Networks [12]. In SFP, these techniques are exercised by using metric measurements, and the fault information obtained by similar software projects [13] or previous versions to construct models to predict faults. Suppose, by using metrics to build a model of fault prediction [14] for the calculation of inheritance of software, cohesion, coupling, size, and complexity. (Efficacy of Inheritance Aspect in Software Fault Prediction—A Survey Paper, page 1)

### response

Berikut beberapa cara yang disebutkan dalam konteks untuk mengukur software quality:

*   Dengan menggunakan formula (4) yang ditemukan dalam sumber [Change-Oriented Open Source Software Process Simulation], di mana q adalah kualitas perangkat lunak, b adalah bug terbuka, dan l adalah kode yang telah berubah secara keseluruhan. Kualitas perangkat lunak diungkapkan oleh tingkat bug, yaitu jumlah bug terbuka dibagi dengan kode yang telah berubah secara keseluruhan.
*   Dengan memeriksa kemampuan review kode yang dilakukan oleh banyak reviewer, terutama ketika dilaksanakan bersamaan dengan pengujian otomatis. Kemampuan review dikatakan dalam bentuk rasio efektifitas review seperti dalam Gambar 7, di mana nilai nol menunjukkan bahwa kode yang telah berubah tidak direview.
*   Dengan menggunakan standar ISO/IEC 25010 yang menetapkan delapan atribut untuk penilaian kualitas perangkat lunak.
*   Dengan mengukur atribut kualitas seperti kompleksitas, keandalan, skalabilitas, fungsi, efisiensi, daya portabilitas, dan kemudahan penggunaan yang menunjukkan karakteristik sebenarnya dari sistem yang diimplementasikan.

### reference


In order to effectively coordinate and evaluate software quality management efforts, software companies use software quality models [34], [37], [44], [45]. The earliest software quality model was proposed by McCall in 1976.

Software quality is calculated in the following formula (4): In formula (4), q is Software quality; b is Open bugs; l is Total changed codes. Software quality is expressed by the bug rate, which is equal to the number of Open bugs divided by the Total changed codes.

Software quality is defined by how closely a software system meets a desired combination of quality attributes [6], [7]. These attributes include complexity, reliability, scalability, functionality, efficiency, portability, usability, and maintainability, each contributing to the system's overall effectiveness [8], [9].

Quality is defined by ISO 8042 [18] as ''the totality of characteristics of an entity that bear on its ability to satisfy stated and implied needs''.

Among the ten studies (7.2%) that discussed software quality attributes, the most frequently mentioned were efficiency, complexity, robustness, performance, and scalability.

In general, quality is considered as the most vital factor for meeting customer expectations and organizational growth [12], [34], [40]. More specifically, software quality is a critical success factor for software development companies [12], [13], [41].

The faults are not uniformly dispersed within the software components. Some classes have a relatively high number of faults as compare to others and are clustered in a limited number of classes [6].

---

## Sample 10

- conversation_id: 14
- user_chat_id: 684
- bot_chat_id: 685

### user_input

Apa hubungan software quality dengan software testing?

### retrieved_context

1. Software quality is defined by how closely a software system meets a desired combination of quality attributes [6], [7]. These attributes include complexity, reliability, scalability, functionality, efficiency, portability, usability, and maintainability, each contributing to the system's overall effectiveness [8], [9]. These quality attributes reflect the actual characteristics of the implemented system [8].

In AI-based systems, quality attributes are critical in shaping architectural decisions [4]. These systems introduce additional challenges, such as model management, accuracy, robustness, and inference latency [3], which the architectural design process must carefully address. Consequently, selecting an appropriate architectural style ensures that AI-based software systems meet their requirements effectively. (Architectural Styles and Quality Attributes in AI-Based Video Software: A Systematic Literature Review, page 1)

2. In order to effectively coordinate and evaluate software quality management efforts, software companies use software quality models [34], [37], [44], [45]. The earliest software quality model was proposed by McCall in 1976. The McCall model was later revised by Boehm and Dromey [41], [44], [46], [47]. Recently developed software quality evaluation models include ISO/IEC 25010 which outlines 8 attributes to be used for software quality assessment. In contrast, the earlier version ISO/IEC 9126 adopts 6 characteristics [44], [45], [48].

Despite being viewed as a useful tool for quality assurance [44], software standards or models lack functionality and practical application owing to the ambiguity involved [37], [47]. Gorla and Lin as cited in [49] propose a software quality assessment model that includes relevance and usefulness (i.e., functionality), usability, maintainability, and reliability attributes. On the other hand, other scholars identify usability, reliability, functionality, performance efficiency, portability, and maintainability as important quality measurements [40], [46]. Similarly, several studies identify functionality, usability, reliability, performance efficiency, and maintainability as the most impactful measures of software quality [14], [41], [43], [45]. Consequently, functionality, usability, performance efficiency, reliability, and maintainability indicators are adopted for the evaluation of software quality in this study. (How Software Quality Mediates the Impact of Intellectual Capital on Commercial Open-Source Software Company Success, page 1)

3. Testing is defined as ''an activity in which a system is executed under specified conditions, the results are observed or recorded, and an evaluation is made of some aspect of the system'' (ISO/IEC 24765, 2006) [6]. In parallel to this definition of testing, a major task of the software development process, software testing is defined as the process of observing and demonstrating the behavior of a software system for compliance with its specifications [7]. As it requires several strategies and techniques with the involvement of several tools and resources, software testing is also considered as a complex task [8]. The background for this study is given below, summarizing the important role of software testing in the software development life cycle, potential impact of software testing strategies, and review studies conducted on software testing. (Evolution of Software Testing Strategies and Trends: Semantic Content Analysis of Software Research Corpus of the Last 40 Years, page 1)

4. Software testing covers several activities of the software development processes starting from the validation of initial requirements through to the acceptance of the end product by the customer [9]. Starting from the requirement specifications, the software testing tasks need to be planned and implemented in different stages of the software development process. Furthermore, software testing needs to be performed during different stages of the software development process for different purposes, such as the testing of the software product lines [10] and the graphical user interface [11]. (Evolution of Software Testing Strategies and Trends: Semantic Content Analysis of Software Research Corpus of the Last 40 Years, page 2)

5. The faults are not uniformly dispersed within the software components. Some classes have a relatively high number of faults as compare to others and are clustered in a limited number of classes [6]. Source code quality is measured through internal metrics whereas the behavior or functionality of the software is measured by external metrics [4]. In general, these two types of metrics are utilized to assess the quality of the software to indicate the degree of reliability of the software. Presently in software engineering, numerous prediction approaches are being used in the research that includes prediction of reuse, prediction of testing effort, prediction of cost, prediction of security, prediction of faults, prediction of quality, and prediction of stress [7]. Out of these, software fault prediction is an emergent research domain where defective classes are identified during the initial phases of development project [8] by utilizing machine learning [9]. Many approaches make use of typical methods of machine learning, which consist of Support Vector Machines (SVM), Naive Bayes (NB) [10], Decision Trees [11], and Neural Networks [12]. In SFP, these techniques are exercised by using metric measurements, and the fault information obtained by similar software projects [13] or previous versions to construct models to predict faults. Suppose, by using metrics to build a model of fault prediction [14] for the calculation of inheritance of software, cohesion, coupling, size, and complexity. (Efficacy of Inheritance Aspect in Software Fault Prediction—A Survey Paper, page 1)

6. Among the ten studies (7.2%) that discussed software quality attributes, the most frequently mentioned were efficiency, complexity, robustness, performance, and scalability. Efficiency was the most commonly reported attribute, appearing in four studies [37], [38], [39], [40], followed by complexity, referenced in three studies [41], [42], [43], while robustness [43], [44], performance [45], and scalability [36] were each mentioned in one or two studies. These studies measured the attributes in different ways across studies. Performance was assessed based on training time, measured in hours per epoch. They evaluated efficiency using response time, computational time, and average response time with prediction rate. Complexity was determined by analyzing the number of parameters in the system. They examined scalability through dataset transfer time to cloud storage and execution time variations under different dataset sizes and processing nodes. Finally, the studies evaluated robustness by measuring prediction accuracy and AUC under various noise conditions. Multiple studies used time cost-the average time required to process a single sample-as a measure of efficiency. Table 4 summarizes the identified quality attributes and their corresponding measurement methods to provide a (Architectural Styles and Quality Attributes in AI-Based Video Software: A Systematic Literature Review, page 1)

7. AI-based software testing refers to the leverage and applications of AI methods and solutions to automatically optimize a software testing process in test strategy selection, test generation, test selection and execution, bug detection and analysis, and quality prediction [39], [42], [47]. It includes different testing activities in AI-based software testing. Due to the complexity of AI software and applications, traditional methods and test tools cannot meet the demands of testing these AI systems. Given this, a more effective method to test AI systems is desirable. (Testing and Quality Validation for AI Software–Perspectives, Issues, and Practices, page 1)

8. Software quality is calculated in the following formula (4):  In formula (4), q is Software quality; b is Open bugs; l is Total changed codes. Software quality is expressed by the bug rate, which is equal to the number of Open bugs divided by the Total changed codes.

In Quality assurance subsystem, Code review by numerous reviewers, particularly when carried out in tandem with automatic test, can significantly, positively impact software quality. Code review in Figure 7 is a ratio of the effectiveness of the review. If it is equal to 0, it means that the changed code is not reviewed. In the following empirical case study (in Section III), we input a random function to analyze its impact. (Change-Oriented Open Source Software Process Simulation, page 1)

### response

Software quality terkait erat dengan software testing. Software testing dapat membantu menentukan kualitas software melalui proses observasi dan evaluasi perilaku sistem perangkat lunak terhadap spesifikasinya. Dengan demikian, software testing memainkan peran penting dalam memastikan bahwa suatu sistem perangkat lunak mencapai kualitas yang diinginkan.

(Sumber: [Source: Evolution of Software Testing Strategies and Trends: Semantic Content Analysis of Software Research Corpus of the Last 40 Years], [Source: Testing and Quality Validation for AI Software–Perspectives, Issues, and Practices])

### reference


Software quality is defined by how closely a software system meets a desired combination of quality attributes [6], [7]. These attributes include complexity, reliability, scalability, functionality, efficiency, portability, usability, and maintainability, each contributing to the system's overall effectiveness [8], [9].

In order to effectively coordinate and evaluate software quality management efforts, software companies use software quality models [34], [37], [44], [45]. The earliest software quality model was proposed by McCall in 1976.

Testing is defined as ''an activity in which a system is executed under specified conditions, the results are observed or recorded, and an evaluation is made of some aspect of the system'' (ISO/IEC 24765, 2006) [6].

Software testing covers several activities of the software development processes starting from the validation of initial requirements through to the acceptance of the end product by the customer [9]. Starting from the requirement specifications, the software testing tasks need to be planned and implemented in different stages of the software development process.

The faults are not uniformly dispersed within the software components. Some classes have a relatively high number of faults as compare to others and are clustered in a limited number of classes [6].

Among the ten studies (7.2%) that discussed software quality attributes, the most frequently mentioned were efficiency, complexity, robustness, performance, and scalability.

AI-based software testing refers to the leverage and applications of AI methods and solutions to automatically optimize a software testing process in test strategy selection, test generation, test selection and execution, bug detection and analysis, and quality prediction [39], [42], [47]. It includes different testing activities in AI-based software testing.

Software quality is calculated in the following formula (4): In formula (4), q is Software quality; b is Open bugs; l is Total changed codes. Software quality is expressed by the bug rate, which is equal to the number of Open bugs divided by the Total changed codes.
