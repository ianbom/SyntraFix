# RAGAS Test Data

File ini digenerate dari tabel `chats`, `chat_references`, dan `document_chunks`.
`retrieved_context` memakai `document_chunks.content` jika tersedia, lalu fallback ke `chat_references.quote`.
`reference` sengaja dikosongkan agar dapat diisi manual.

## Sample 46

- conversation_id: 14
- user_chat_id: 768
- bot_chat_id: 769

### user_input

Apa itu software metrics?

### retrieved_context

1. Measurement is needed to validate the effectiveness of software development process. The phrase software metrics describes measurements made on an artifact of software whereas a software artifact has two significant elements: the coded implementation, and the document of its design specification. The initially calculated McCabe, Halstead, and Albrecht metrics, presented during the 1970s, were typically constructed on the coded final software products. Examples of software science metrics include [1] function point analysis [2], and cyclomatic complexity metric [3], which predominated in the early 1980s to measure software product. (Efficacy of Inheritance Aspect in Software Fault Prediction—A Survey Paper, page 1)

2. Software metrics are foundation to quantify complexity, quality of software, and project costs with effort estimation. Function points and cyclomatic complexity are traditional metrics. These are being utilized in the paradigm of procedure language. Nonetheless, these may not merely be utilized in the context of object-oriented [21]. The procedural languages are less complex while comparing with object-oriented programming language [22]. The majority of studies specified hurdles in moving from a procedural approach towards an objectoriented paradigm [23].In object-oriented, it is problematic to comprehend how inheritance, abstraction, and encapsulation associated with each other. (Efficacy of Inheritance Aspect in Software Fault Prediction—A Survey Paper, page 1)

3. Software metrics make it easy for developers to audit and monitor the quality of software design as the project progresses. In addition, predicting the probability of defective classes is needed to help the software engineers during development to enhance the quality of software and reduce testing and maintenance costs. For example, in order to increase the productivity of software testing, software evaluators can plan tests based on the parts most prone to faults.

TABLE 1. List of inheritance metrics.

Software metrics and fault data for an earlier software version are utilized to make an SFP model for the next software version [83]. When a software has faults, it leades to a disaster because it has a significant human dependency on it. Therefore, there is an emerging requirement for software without faults. Software Companies are expanding to discover faults in software. Producing software without faults is a challenging job. To lower costs and improve software usefulness, it is vital to classify classes which are faulty. Many software metrics are proposed by the researchers to gauge the software quality. In object-oriented paradigm, metrics are beneficial for software engineers to make additional information associated with software quality available. Quality of software can also be monitored through metrics, while software evaluators use metrics to increase the effectiveness of testing [84]. (Experimental Validation of Inheritance Metrics’ Impact on Software Fault Prediction, page 3)

4. TABLE 2. Class-level software metric used in this study.

Tabel ini memuat beberapa metrik kelas untuk prediksi kesalahan perangkat lunak. Data tabel menunjukkan bahwa ada dua dataset utama: Software Metrics dan Full Dataset. Kedua dataset tersebut berbeda dalam hal variabel independen yang digunakan, yaitu ESM (Error-Severity Metric) values dan software metrics yang diekstraksi dari modul perangkat lunak.

Pada tabel ini, kita dapat melihat bahwa terdapat tiga jenis metrik ESM: IndexOutOfBounds, NullPointer, dan ClassCast. Masing-masing metrik tersebut memiliki nilai-nilai yang berbeda-beda pada kedua dataset. Pada Software Metrics Dataset, variabel independen hanya mencakup software metrics, sedangkan pada Full Dataset juga termasuk ESM values.

Dengan memperhatikan tabel ini, kita dapat menyimpulkan bahwa peneliti menggunakan metrik-metrik tersebut untuk memprediksi kesalahan perangkat lunak. Pada dataset yang lebih lengkap (Full Dataset), penulis juga melibatkan ESM values sebagai variabel independen tambahan. Hal ini menunjukkan bahwa penulis ingin mengetahui bagaimana pengaruh nilai-nilai ESM terhadap performa model pelatihan machine learning.

Dalam konteks yang lebih luas, tabel ini memberikan gambaran tentang cara peneliti menggunakan metrik kelas untuk prediksi kesalahan perangkat lunak. Penemuan penulis dapat berguna dalam meningkatkan akurasi model pemodelan perangkat lunak dan mengidentifikasi potensi masalah yang mungkin terjadi pada sistem. (Error-Type—A Novel Set of Software Metrics for Software Fault Prediction, page 6)

5. The software metrics are the basis to measure the complexity, quality of software and estimate cost along with efforts of projects. Traditional metrics such as function point and cyclomatic complexity have been employed in the procedure paradigm. But, these are not simply used in object-oriented paradigm [39], [40]. Object Oriented programming is complex while comparing it with procedural languages [41]. Most studies stated difficulty in switching to the object-oriented paradigm from the procedural approach [42]. In Objectoriented Programming, it is difficult to understand how features, for example abstraction, inheritance and encapsulation relate to each other [43]. (Experimental Validation of Inheritance Metrics’ Impact on Software Fault Prediction, page 1)

6. The goal of this research question is to investigate the usefulness, relevance, and potential issues of ESM values in software fault prediction when being incorporated with the other software metrics.

The rest of the paper is organised as follows. Section II contains related work. Section III describes the proposed methodology. Section IV outlines the results of the experiments and discusses the threats to validity. Section V concludes the paper and provides the directions for the future research. (Error-Type—A Novel Set of Software Metrics for Software Fault Prediction, page 2)

7. TABLE 2. Frequently Used Metrics in Software Fault Prediction.

Tabel ini memuat beberapa studi terkait penggunaan metrik dalam prediksi kegagalan perangkat lunak. Lima belas penelitian yang disebutkan menunjukkan bahwa beberapa metrik telah digunakan secara luas dalam prediksi kegagalan, seperti metrik yang terkait dengan sifat objek-oriented dan perilaku pengguna.

Variabel utama di tabel ini meliputi nama penulis, judul penelitian, metode yang digunakan, serta hasil yang diperoleh. Nilai penting dari tabel ini adalah penemuan bahwa beberapa metrik khususnya terkait dengan sifat objek-oriented telah terbukti efektif dalam prediksi kegagalan perangkat lunak.

Pola penting dapat dilihat dari kemunculan istilah-istilah seperti "C&K metrics" dan "Li and Henry," yang mengindikasikan bahwa ada metrik yang secara konsisten digunakan dalam penelitian-penelitian ini. Selain itu, juga terlihat bahwa beberapa penulis menggunakan kombinasi berbagai metode analisis untuk mencapai hasil prediksi yang lebih akurat.

Insight singkat dari tabel ini adalah pentingnya penggunaan metrik-metrik tertentu dalam prediksi kegagalan perangkat lunak. Dengan demikian, penelitian ini menunjukkan bahwa dengan memahami dan menggunakan metrik yang tepat, kita dapat meningkatkan akurasi prediksi kegagalan perangkat lunak. (Efficacy of Inheritance Aspect in Software Fault Prediction—A Survey Paper, page 13)

8. In the SLR, we generalized metrics collection methods among six categories. The collected metrics are a key input for evaluation, prediction, characterization, and improvement of software development process. In this survey, majority of the organizations only collect most common FIGURE 16. Frequency of metrics collection methods in software organizations.

metrics (23%) or necessary metrics (30%) for software process improvement. The SMEs (20%), large (22%) and very large (37%) organizations collect metrics that are necessary for software process improvement. The most common metrics are collected by SMEs (30%), large (30%) and very large (11%) organizations as shown in Figure 16. The use of measurement tools and expert judgment is used by 14% of organizations. The use of automated tools, measurement models and expert judgment is under 15% among the organizations. The use of measurement models is least used method for metrics collection while on the other hand, there are 35 measurement models proposed in literature. (An Evaluation of Software Measurement Processes in Pakistani Software Industry, page 11)

### response

Software metrics adalah pengukuran yang dibuat pada artefak perangkat lunak untuk mengukur kompleksitas, kualitas perangkat lunak dan estimasi biaya serta upaya proyek.

### reference


Measurement is needed to validate the effectiveness of software development process. The phrase software metrics describes measurements made on an artifact of software whereas a software artifact has two significant elements: the coded implementation, and the document of its design specification.

Software metrics are foundation to quantify complexity, quality of software, and project costs with effort estimation. Function points and cyclomatic complexity are traditional metrics.

Software metrics make it easy for developers to audit and monitor the quality of software design as the project progresses. In addition, predicting the probability of defective classes is needed to help the software engineers during development to enhance the quality of software and reduce testing and maintenance costs.

Class-level software metric used in this study. Tabel ini memuat beberapa metrik kelas untuk prediksi kesalahan perangkat lunak.

The software metrics are the basis to measure the complexity, quality of software and estimate cost along with efforts of projects. Traditional metrics such as function point and cyclomatic complexity have been employed in the procedure paradigm.

The goal of this research question is to investigate the usefulness, relevance, and potential issues of ESM values in software fault prediction when being incorporated with the other software metrics. The rest of the paper is organised as follows.

Frequently Used Metrics in Software Fault Prediction. Tabel ini memuat beberapa studi terkait penggunaan metrik dalam prediksi kegagalan perangkat lunak.

In the SLR, we generalized metrics collection methods among six categories. The collected metrics are a key input for evaluation, prediction, characterization, and improvement of software development process.

---

## Sample 47

- conversation_id: 14
- user_chat_id: 770
- bot_chat_id: 771

### user_input

Mengapa software metrics penting?

### retrieved_context

1. Measurement is needed to validate the effectiveness of software development process. The phrase software metrics describes measurements made on an artifact of software whereas a software artifact has two significant elements: the coded implementation, and the document of its design specification. The initially calculated McCabe, Halstead, and Albrecht metrics, presented during the 1970s, were typically constructed on the coded final software products. Examples of software science metrics include [1] function point analysis [2], and cyclomatic complexity metric [3], which predominated in the early 1980s to measure software product. (Efficacy of Inheritance Aspect in Software Fault Prediction—A Survey Paper, page 1)

2. Software metrics make it easy for developers to audit and monitor the quality of software design as the project progresses. In addition, predicting the probability of defective classes is needed to help the software engineers during development to enhance the quality of software and reduce testing and maintenance costs. For example, in order to increase the productivity of software testing, software evaluators can plan tests based on the parts most prone to faults.

TABLE 1. List of inheritance metrics.

Software metrics and fault data for an earlier software version are utilized to make an SFP model for the next software version [83]. When a software has faults, it leades to a disaster because it has a significant human dependency on it. Therefore, there is an emerging requirement for software without faults. Software Companies are expanding to discover faults in software. Producing software without faults is a challenging job. To lower costs and improve software usefulness, it is vital to classify classes which are faulty. Many software metrics are proposed by the researchers to gauge the software quality. In object-oriented paradigm, metrics are beneficial for software engineers to make additional information associated with software quality available. Quality of software can also be monitored through metrics, while software evaluators use metrics to increase the effectiveness of testing [84]. (Experimental Validation of Inheritance Metrics’ Impact on Software Fault Prediction, page 3)

3. Metrics and roles play a fundamental role in SD, as supported by GAI. The utilization of these metrics enables the establishment of an objective for evaluating the quality of AI-generated codes, including their accuracy and efficiency. These measures empower developers to evaluate the congruence between the resulting artifacts and original objectives, thereby identifying opportunities for enhancement [21], [22]. More broadly, metrics support software engineering quality assessment by quantifying the key characteristics of the development process, including efficiency and maintainability. A review of the literature reveals that commonly reported metrics include structural complexity measures, which assess software architecture using indicators such as the number of modules and interconnections [23]. Quality metrics are used to forecast software reliability and support decision-making throughout the SDLC [24]. Finally, productivity metrics are reported, and these assess the impact of GAI-based tools on development speed, quality, and overall efficiency [6], [25]. (Generative Artificial Intelligence for Software Development Using ISO/IEC 29110 Basic Profile: Gaps and Opportunities, page 2)

4. Metrics and roles play a fundamental role in SD, as supported by GAI. The utilization of these metrics enables the establishment of an objective for evaluating the quality of AI-generated codes, including their accuracy and efficiency. These measures empower developers to evaluate the congruence between the resulting artifacts and original objectives, thereby identifying opportunities for enhancement [21], [22]. More broadly, metrics support software engineering quality assessment by quantifying the key characteristics of the development process, including efficiency and maintainability. A review of the literature reveals that commonly reported metrics include structural complexity measures, which assess software architecture using indicators such as the number of modules and interconnections [23]. Quality metrics are used to forecast software reliability and support decision-making throughout the SDLC [24]. Finally, productivity metrics are reported, and these assess the impact of GAI-based tools on development speed, quality, and overall efficiency [6], [25]. (Generative Artificial Intelligence for Software Development Using ISO/IEC 29110 Basic Profile: Gaps and Opportunities, page 2)

5. Software metrics are foundation to quantify complexity, quality of software, and project costs with effort estimation. Function points and cyclomatic complexity are traditional metrics. These are being utilized in the paradigm of procedure language. Nonetheless, these may not merely be utilized in the context of object-oriented [21]. The procedural languages are less complex while comparing with object-oriented programming language [22]. The majority of studies specified hurdles in moving from a procedural approach towards an objectoriented paradigm [23].In object-oriented, it is problematic to comprehend how inheritance, abstraction, and encapsulation associated with each other. (Efficacy of Inheritance Aspect in Software Fault Prediction—A Survey Paper, page 1)

6. The software engineering (SE) community is continuously looking for better and more efficient ways of building high-quality software systems. However, in practice, the strong emphasis on time to market tends to ignore many, well-known SE recommendations. That is, practitioners focus more on programming as compared to requirements gathering, planning, specification, architecture, design, and documentation -all of which are ultimately known to greatly benefit the cost-effectiveness and quality of software systems. Lack of human resources is often cited as the main reason for doing so. Herein lies the great potential for machine learning (ML) since its algorithms are proven to be most befitting to problem domains that aim to replicate human behavior. Hence, it stands to reason that human-centric SE activities should also benefit from ML [1]. (A Literature Review of Using Machine Learning in Software Development Life Cycle Stages, page 1)

7. • Most of the organizations use necessary and most commonly used metrics and expert judgment instead of measurement models, and automated tools.

• Duration (32%), cost (27%), and effort (27%) are the most measured attributes.

• 89% of the organizations don't use real-time metrics (e.g., cyclomatic complexity, dynamic function calls, no of unused objects and variables) to monitor and control the actual software development progress.

• A measurement glossary is completely maintained by 38% of the organizations, while 19% partially and 16% don't use measurement glossary at all.

• Less than 50% of the organizations frequently use past data for prediction.

• 58% of software organizations don't have any metrics validation criteria. (An Evaluation of Software Measurement Processes in Pakistani Software Industry, page 1)

8. In another context, AbdeenMod+RM metrics introduced an acceptable satisfaction in the fault prediction modeling. This satisfaction may increase in the implementation of a large number of alternative metrics and other techniques used in diverse aspects to present different results, which may reflect the overall recommendations of the research.

Modularity metrics refers to the significantly negative interrelationship by modularity indicators IPCI and IPGF. This may improve the performance and accuracy or less effort needed to predict by assuming a new modularity metrics at the system level and adapting current modularity indicators specified in other perspectives (e.g., complex networks). Furthermore, the architecture-sensitive metrics for code anomalies discovery provides the majority of awareness to engineers for the existence of the smells code elements that are more significant to the architecture design than the most traditional metrics that are depending on source code and based on static code metrics combination. This means that the developers and engineers could detect and repair such anomalies promptly.

Therefore, more studies are needed in this field for other metrics to be analyzed in order to provide the most appropriate architecture without any impact of the size bias. Furthermore, there is a need for metrics that have a great ability to discover the inconsistent classes affected by the degradation from the consistent classes. In addition, there is a need to identify the effort required for the metrics strategy to architecturally detect related anomalies and also to derive more metrics that may have an impact on the quality relationships of other software that are closely related to architectural problems. (Software Architecture Degradation in Open Source Software: A Systematic Literature Review, page 22)

### response

Software metrics penting karena:

* Membantu pengembang untuk audit dan monitor kualitas perancangan software selama proyek berlangsung.
* Memprediksi kemungkinan klas yang bermasalah sehingga dapat membantu para insinyur software untuk meningkatkan kualitas software dan mengurangi biaya pengujian dan perawatan.
* Mengukur kompleksitas, kualitas software, dan biaya proyek dengan perkiraan upah.

### reference


Measurement is needed to validate the effectiveness of software development process. The phrase software metrics describes measurements made on an artifact of software whereas a software artifact has two significant elements: the coded implementation, and the document of its design specification.

Software metrics make it easy for developers to audit and monitor the quality of software design as the project progresses. In addition, predicting the probability of defective classes is needed to help the software engineers during development to enhance the quality of software and reduce testing and maintenance costs.

Metrics and roles play a fundamental role in SD, as supported by GAI. The utilization of these metrics enables the establishment of an objective for evaluating the quality of AI-generated codes, including their accuracy and efficiency.

Software metrics are foundation to quantify complexity, quality of software, and project costs with effort estimation. Function points and cyclomatic complexity are traditional metrics.

The software engineering (SE) community is continuously looking for better and more efficient ways of building high-quality software systems. However, in practice, the strong emphasis on time to market tends to ignore many, well-known SE recommendations.

• Most of the organizations use necessary and most commonly used metrics and expert judgment instead of measurement models, and automated tools. • Duration (32%), cost (27%), and effort (27%) are the most measured attributes. • 89% of the organizations don't use real-time metrics (e.g., cyclomatic complexity, dynamic function calls, no of unused objects and variables) to monitor and control the actual software...

In another context, AbdeenMod+RM metrics introduced an acceptable satisfaction in the fault prediction modeling. This satisfaction may increase in the implementation of a large number of alternative metrics and other techniques used in diverse aspects to present different results, which may reflect the overall recommendations of the research.

---

## Sample 48

- conversation_id: 14
- user_chat_id: 772
- bot_chat_id: 773

### user_input

Apa contoh software metrics?

### retrieved_context

1. Measurement is needed to validate the effectiveness of software development process. The phrase software metrics describes measurements made on an artifact of software whereas a software artifact has two significant elements: the coded implementation, and the document of its design specification. The initially calculated McCabe, Halstead, and Albrecht metrics, presented during the 1970s, were typically constructed on the coded final software products. Examples of software science metrics include [1] function point analysis [2], and cyclomatic complexity metric [3], which predominated in the early 1980s to measure software product. (Efficacy of Inheritance Aspect in Software Fault Prediction—A Survey Paper, page 1)

2. Software metrics are foundation to quantify complexity, quality of software, and project costs with effort estimation. Function points and cyclomatic complexity are traditional metrics. These are being utilized in the paradigm of procedure language. Nonetheless, these may not merely be utilized in the context of object-oriented [21]. The procedural languages are less complex while comparing with object-oriented programming language [22]. The majority of studies specified hurdles in moving from a procedural approach towards an objectoriented paradigm [23].In object-oriented, it is problematic to comprehend how inheritance, abstraction, and encapsulation associated with each other. (Efficacy of Inheritance Aspect in Software Fault Prediction—A Survey Paper, page 1)

3. Software metrics make it easy for developers to audit and monitor the quality of software design as the project progresses. In addition, predicting the probability of defective classes is needed to help the software engineers during development to enhance the quality of software and reduce testing and maintenance costs. For example, in order to increase the productivity of software testing, software evaluators can plan tests based on the parts most prone to faults.

TABLE 1. List of inheritance metrics.

Software metrics and fault data for an earlier software version are utilized to make an SFP model for the next software version [83]. When a software has faults, it leades to a disaster because it has a significant human dependency on it. Therefore, there is an emerging requirement for software without faults. Software Companies are expanding to discover faults in software. Producing software without faults is a challenging job. To lower costs and improve software usefulness, it is vital to classify classes which are faulty. Many software metrics are proposed by the researchers to gauge the software quality. In object-oriented paradigm, metrics are beneficial for software engineers to make additional information associated with software quality available. Quality of software can also be monitored through metrics, while software evaluators use metrics to increase the effectiveness of testing [84]. (Experimental Validation of Inheritance Metrics’ Impact on Software Fault Prediction, page 3)

4. In the SLR, we generalized metrics collection methods among six categories. The collected metrics are a key input for evaluation, prediction, characterization, and improvement of software development process. In this survey, majority of the organizations only collect most common FIGURE 16. Frequency of metrics collection methods in software organizations.

metrics (23%) or necessary metrics (30%) for software process improvement. The SMEs (20%), large (22%) and very large (37%) organizations collect metrics that are necessary for software process improvement. The most common metrics are collected by SMEs (30%), large (30%) and very large (11%) organizations as shown in Figure 16. The use of measurement tools and expert judgment is used by 14% of organizations. The use of automated tools, measurement models and expert judgment is under 15% among the organizations. The use of measurement models is least used method for metrics collection while on the other hand, there are 35 measurement models proposed in literature. (An Evaluation of Software Measurement Processes in Pakistani Software Industry, page 11)

5. The software metrics are the basis to measure the complexity, quality of software and estimate cost along with efforts of projects. Traditional metrics such as function point and cyclomatic complexity have been employed in the procedure paradigm. But, these are not simply used in object-oriented paradigm [39], [40]. Object Oriented programming is complex while comparing it with procedural languages [41]. Most studies stated difficulty in switching to the object-oriented paradigm from the procedural approach [42]. In Objectoriented Programming, it is difficult to understand how features, for example abstraction, inheritance and encapsulation relate to each other [43]. (Experimental Validation of Inheritance Metrics’ Impact on Software Fault Prediction, page 1)

6. There is a long history of research on metrics programs (MPs) [24], and plenty of literature recommending success factors for their implementation [17], [28], [34], [44]. However, literature on SMEs using MPs in the context of Agile is rather scarce. Moreover, the literature on measuring software processes and their role in improving SME processes is even scarcer. Measuring software processes with the use of process metrics enables objective and quantitative evaluation of software processes, which can lead to continuous improvement and learning [34], [42]. However, measuring process metrics is a challenge [43]. Software processes are inherently complex and intangible, which makes their measurement more difficult than their product counterparts [19], [41]. Ideally, measurement activities should consume little effort and time, while being adequate enough to meet an organization's measurement demands. Software organizations need to weigh in cost-efficiency while prioritizing measurement objectives and targets. SMEs have the added constraints of limited budget, ambitious deadlines, and short-term strategy [45]. Due to these reasons, measuring software processes, especially in an SME, becomes a bigger challenge. (Measuring and Improving Agile Processes in a Small-Size Software Development Company, page 3)

7. Kupiainen et al. [22] conducted a systematic review of the use and impact of software metrics in ASD in industry. The authors reported that software metrics are mainly used for sprint planning, tracking progress, improving software quality, fixing software process, and motivating people. The authors reported that metrics like velocity, effort estimation, customer satisfaction, defect count, technical debt and build are used prominently in ASD. In their systematic review, Tahir et al. [46] observed that metrics for defects, effort, size, duration, productivity, employee commitment, and customer satisfaction are commonly reported in the state of the art. These findings complement another review by Gómez et al. [15], where complexity and size were found to be the most measured attributes in MPs. Other usage of metrics in ASD discussed in the literature are for planning and tracking software development [22], understanding development performance and product quality [48], measuring process quality [50], estimating effort [47], and reporting progress and quality to stakeholders not involved in the actual development [4]. Taken together, metrics targeting sprint planning, fixing software process, effort estimation, development performance, and software defects can be used to measure an organization's process performance. However, this objective is not expressly stated in any of the reviews mentioned above. On the contrary, [22] remarked that more studies are needed to explore the rationale behind utilizing the metrics the authors found in their review. (Measuring and Improving Agile Processes in a Small-Size Software Development Company, page 3)

8. TABLE 2. Class-level software metric used in this study.

Tabel ini memuat beberapa metrik kelas untuk prediksi kesalahan perangkat lunak. Data tabel menunjukkan bahwa ada dua dataset utama: Software Metrics dan Full Dataset. Kedua dataset tersebut berbeda dalam hal variabel independen yang digunakan, yaitu ESM (Error-Severity Metric) values dan software metrics yang diekstraksi dari modul perangkat lunak.

Pada tabel ini, kita dapat melihat bahwa terdapat tiga jenis metrik ESM: IndexOutOfBounds, NullPointer, dan ClassCast. Masing-masing metrik tersebut memiliki nilai-nilai yang berbeda-beda pada kedua dataset. Pada Software Metrics Dataset, variabel independen hanya mencakup software metrics, sedangkan pada Full Dataset juga termasuk ESM values.

Dengan memperhatikan tabel ini, kita dapat menyimpulkan bahwa peneliti menggunakan metrik-metrik tersebut untuk memprediksi kesalahan perangkat lunak. Pada dataset yang lebih lengkap (Full Dataset), penulis juga melibatkan ESM values sebagai variabel independen tambahan. Hal ini menunjukkan bahwa penulis ingin mengetahui bagaimana pengaruh nilai-nilai ESM terhadap performa model pelatihan machine learning.

Dalam konteks yang lebih luas, tabel ini memberikan gambaran tentang cara peneliti menggunakan metrik kelas untuk prediksi kesalahan perangkat lunak. Penemuan penulis dapat berguna dalam meningkatkan akurasi model pemodelan perangkat lunak dan mengidentifikasi potensi masalah yang mungkin terjadi pada sistem. (Error-Type—A Novel Set of Software Metrics for Software Fault Prediction, page 6)

### response

Berikut beberapa contoh software metrics:

• Function point analysis
• Cyclomatic complexity metric

### reference


Measurement is needed to validate the effectiveness of software development process. The phrase software metrics describes measurements made on an artifact of software whereas a software artifact has two significant elements: the coded implementation, and the document of its design specification.

Software metrics are foundation to quantify complexity, quality of software, and project costs with effort estimation. Function points and cyclomatic complexity are traditional metrics.

Software metrics make it easy for developers to audit and monitor the quality of software design as the project progresses. In addition, predicting the probability of defective classes is needed to help the software engineers during development to enhance the quality of software and reduce testing and maintenance costs.

In the SLR, we generalized metrics collection methods among six categories. The collected metrics are a key input for evaluation, prediction, characterization, and improvement of software development process.

The software metrics are the basis to measure the complexity, quality of software and estimate cost along with efforts of projects. Traditional metrics such as function point and cyclomatic complexity have been employed in the procedure paradigm.

There is a long history of research on metrics programs (MPs) [24], and plenty of literature recommending success factors for their implementation [17], [28], [34], [44]. However, literature on SMEs using MPs in the context of Agile is rather scarce.

Kupiainen et al. [22] conducted a systematic review of the use and impact of software metrics in ASD in industry. The authors reported that software metrics are mainly used for sprint planning, tracking progress, improving software quality, fixing software process, and motivating people.

Class-level software metric used in this study. Tabel ini memuat beberapa metrik kelas untuk prediksi kesalahan perangkat lunak.

---

## Sample 49

- conversation_id: 14
- user_chat_id: 774
- bot_chat_id: 775

### user_input

Bagaimana software metrics digunakan untuk mengukur kualitas software?

### retrieved_context

1. Measurement is needed to validate the effectiveness of software development process. The phrase software metrics describes measurements made on an artifact of software whereas a software artifact has two significant elements: the coded implementation, and the document of its design specification. The initially calculated McCabe, Halstead, and Albrecht metrics, presented during the 1970s, were typically constructed on the coded final software products. Examples of software science metrics include [1] function point analysis [2], and cyclomatic complexity metric [3], which predominated in the early 1980s to measure software product. (Efficacy of Inheritance Aspect in Software Fault Prediction—A Survey Paper, page 1)

2. Software metrics make it easy for developers to audit and monitor the quality of software design as the project progresses. In addition, predicting the probability of defective classes is needed to help the software engineers during development to enhance the quality of software and reduce testing and maintenance costs. For example, in order to increase the productivity of software testing, software evaluators can plan tests based on the parts most prone to faults.

TABLE 1. List of inheritance metrics.

Software metrics and fault data for an earlier software version are utilized to make an SFP model for the next software version [83]. When a software has faults, it leades to a disaster because it has a significant human dependency on it. Therefore, there is an emerging requirement for software without faults. Software Companies are expanding to discover faults in software. Producing software without faults is a challenging job. To lower costs and improve software usefulness, it is vital to classify classes which are faulty. Many software metrics are proposed by the researchers to gauge the software quality. In object-oriented paradigm, metrics are beneficial for software engineers to make additional information associated with software quality available. Quality of software can also be monitored through metrics, while software evaluators use metrics to increase the effectiveness of testing [84]. (Experimental Validation of Inheritance Metrics’ Impact on Software Fault Prediction, page 3)

3. In order to effectively coordinate and evaluate software quality management efforts, software companies use software quality models [34], [37], [44], [45]. The earliest software quality model was proposed by McCall in 1976. The McCall model was later revised by Boehm and Dromey [41], [44], [46], [47]. Recently developed software quality evaluation models include ISO/IEC 25010 which outlines 8 attributes to be used for software quality assessment. In contrast, the earlier version ISO/IEC 9126 adopts 6 characteristics [44], [45], [48].

Despite being viewed as a useful tool for quality assurance [44], software standards or models lack functionality and practical application owing to the ambiguity involved [37], [47]. Gorla and Lin as cited in [49] propose a software quality assessment model that includes relevance and usefulness (i.e., functionality), usability, maintainability, and reliability attributes. On the other hand, other scholars identify usability, reliability, functionality, performance efficiency, portability, and maintainability as important quality measurements [40], [46]. Similarly, several studies identify functionality, usability, reliability, performance efficiency, and maintainability as the most impactful measures of software quality [14], [41], [43], [45]. Consequently, functionality, usability, performance efficiency, reliability, and maintainability indicators are adopted for the evaluation of software quality in this study. (How Software Quality Mediates the Impact of Intellectual Capital on Commercial Open-Source Software Company Success, page 1)

4. Metrics and roles play a fundamental role in SD, as supported by GAI. The utilization of these metrics enables the establishment of an objective for evaluating the quality of AI-generated codes, including their accuracy and efficiency. These measures empower developers to evaluate the congruence between the resulting artifacts and original objectives, thereby identifying opportunities for enhancement [21], [22]. More broadly, metrics support software engineering quality assessment by quantifying the key characteristics of the development process, including efficiency and maintainability. A review of the literature reveals that commonly reported metrics include structural complexity measures, which assess software architecture using indicators such as the number of modules and interconnections [23]. Quality metrics are used to forecast software reliability and support decision-making throughout the SDLC [24]. Finally, productivity metrics are reported, and these assess the impact of GAI-based tools on development speed, quality, and overall efficiency [6], [25]. (Generative Artificial Intelligence for Software Development Using ISO/IEC 29110 Basic Profile: Gaps and Opportunities, page 2)

5. Metrics and roles play a fundamental role in SD, as supported by GAI. The utilization of these metrics enables the establishment of an objective for evaluating the quality of AI-generated codes, including their accuracy and efficiency. These measures empower developers to evaluate the congruence between the resulting artifacts and original objectives, thereby identifying opportunities for enhancement [21], [22]. More broadly, metrics support software engineering quality assessment by quantifying the key characteristics of the development process, including efficiency and maintainability. A review of the literature reveals that commonly reported metrics include structural complexity measures, which assess software architecture using indicators such as the number of modules and interconnections [23]. Quality metrics are used to forecast software reliability and support decision-making throughout the SDLC [24]. Finally, productivity metrics are reported, and these assess the impact of GAI-based tools on development speed, quality, and overall efficiency [6], [25]. (Generative Artificial Intelligence for Software Development Using ISO/IEC 29110 Basic Profile: Gaps and Opportunities, page 2)

6. Kupiainen et al. [22] conducted a systematic review of the use and impact of software metrics in ASD in industry. The authors reported that software metrics are mainly used for sprint planning, tracking progress, improving software quality, fixing software process, and motivating people. The authors reported that metrics like velocity, effort estimation, customer satisfaction, defect count, technical debt and build are used prominently in ASD. In their systematic review, Tahir et al. [46] observed that metrics for defects, effort, size, duration, productivity, employee commitment, and customer satisfaction are commonly reported in the state of the art. These findings complement another review by Gómez et al. [15], where complexity and size were found to be the most measured attributes in MPs. Other usage of metrics in ASD discussed in the literature are for planning and tracking software development [22], understanding development performance and product quality [48], measuring process quality [50], estimating effort [47], and reporting progress and quality to stakeholders not involved in the actual development [4]. Taken together, metrics targeting sprint planning, fixing software process, effort estimation, development performance, and software defects can be used to measure an organization's process performance. However, this objective is not expressly stated in any of the reviews mentioned above. On the contrary, [22] remarked that more studies are needed to explore the rationale behind utilizing the metrics the authors found in their review. (Measuring and Improving Agile Processes in a Small-Size Software Development Company, page 3)

7. The software metrics are the basis to measure the complexity, quality of software and estimate cost along with efforts of projects. Traditional metrics such as function point and cyclomatic complexity have been employed in the procedure paradigm. But, these are not simply used in object-oriented paradigm [39], [40]. Object Oriented programming is complex while comparing it with procedural languages [41]. Most studies stated difficulty in switching to the object-oriented paradigm from the procedural approach [42]. In Objectoriented Programming, it is difficult to understand how features, for example abstraction, inheritance and encapsulation relate to each other [43]. (Experimental Validation of Inheritance Metrics’ Impact on Software Fault Prediction, page 1)

8. Soini [8] presented a survey to investigate the use of software measurement in the Finish software industry. The problems, challenges, limitations are evaluated. There is an overlap between the metrics used for measuring processes and products and most of the process metrics are used for product measurement too which can affect the effectiveness of decision making. Most of the metrics are extracted from the data that was not collected with the intention/context of measurement. Metrics are not collected for their intended use at some management level e.g., middle or upper management. Most of the metrics are lagging (calculated at the end of a process) but there is a strong need of leading metrics (real-time) that can support effective monitoring and controlling. The metrics selection method is based on the information system available for project management in software organizations, or metrics are extracted from already collected data. The metrics are mostly collected to characterize and evaluate while they are rarely used for prediction and improvement of software processes, products, and resources. Most of the metrics are collected and analyzed regarding processes and products entities while resource metrics are least collected and analyzed. We have also evaluated related issues in Pakistani Software industry including purposes of measurement processes, types of metrics, real-time metrics, scope of measurement process, availability of measurement tools, and defined measurement process (Section 3.1). (An Evaluation of Software Measurement Processes in Pakistani Software Industry, page 3)

### response

Software metrics digunakan untuk mengukur kompleksitas, kualitas, dan perkiraan biaya serta upaya proyek. Mereka membantu dalam estimasi biaya dan waktu proyek, pengujian, dan pemeliharaan software. Selain itu, mereka juga membantu developer dalam meningkatkan efisiensi proses pengembangan perangkat lunak.

### reference


Measurement is needed to validate the effectiveness of software development process. The phrase software metrics describes measurements made on an artifact of software whereas a software artifact has two significant elements: the coded implementation, and the document of its design specification.

Software metrics make it easy for developers to audit and monitor the quality of software design as the project progresses. In addition, predicting the probability of defective classes is needed to help the software engineers during development to enhance the quality of software and reduce testing and maintenance costs.

In order to effectively coordinate and evaluate software quality management efforts, software companies use software quality models [34], [37], [44], [45]. The earliest software quality model was proposed by McCall in 1976.

Metrics and roles play a fundamental role in SD, as supported by GAI. The utilization of these metrics enables the establishment of an objective for evaluating the quality of AI-generated codes, including their accuracy and efficiency.

Kupiainen et al. [22] conducted a systematic review of the use and impact of software metrics in ASD in industry. The authors reported that software metrics are mainly used for sprint planning, tracking progress, improving software quality, fixing software process, and motivating people.

The software metrics are the basis to measure the complexity, quality of software and estimate cost along with efforts of projects. Traditional metrics such as function point and cyclomatic complexity have been employed in the procedure paradigm.

Soini [8] presented a survey to investigate the use of software measurement in the Finish software industry. The problems, challenges, limitations are evaluated.

---

## Sample 50

- conversation_id: 14
- user_chat_id: 776
- bot_chat_id: 777

### user_input

Bagaimana software metrics membantu software testing?

### retrieved_context

1. Software metrics make it easy for developers to audit and monitor the quality of software design as the project progresses. In addition, predicting the probability of defective classes is needed to help the software engineers during development to enhance the quality of software and reduce testing and maintenance costs. For example, in order to increase the productivity of software testing, software evaluators can plan tests based on the parts most prone to faults.

TABLE 1. List of inheritance metrics.

Software metrics and fault data for an earlier software version are utilized to make an SFP model for the next software version [83]. When a software has faults, it leades to a disaster because it has a significant human dependency on it. Therefore, there is an emerging requirement for software without faults. Software Companies are expanding to discover faults in software. Producing software without faults is a challenging job. To lower costs and improve software usefulness, it is vital to classify classes which are faulty. Many software metrics are proposed by the researchers to gauge the software quality. In object-oriented paradigm, metrics are beneficial for software engineers to make additional information associated with software quality available. Quality of software can also be monitored through metrics, while software evaluators use metrics to increase the effectiveness of testing [84]. (Experimental Validation of Inheritance Metrics’ Impact on Software Fault Prediction, page 3)

2. Measurement is needed to validate the effectiveness of software development process. The phrase software metrics describes measurements made on an artifact of software whereas a software artifact has two significant elements: the coded implementation, and the document of its design specification. The initially calculated McCabe, Halstead, and Albrecht metrics, presented during the 1970s, were typically constructed on the coded final software products. Examples of software science metrics include [1] function point analysis [2], and cyclomatic complexity metric [3], which predominated in the early 1980s to measure software product. (Efficacy of Inheritance Aspect in Software Fault Prediction—A Survey Paper, page 1)

3. Metrics and roles play a fundamental role in SD, as supported by GAI. The utilization of these metrics enables the establishment of an objective for evaluating the quality of AI-generated codes, including their accuracy and efficiency. These measures empower developers to evaluate the congruence between the resulting artifacts and original objectives, thereby identifying opportunities for enhancement [21], [22]. More broadly, metrics support software engineering quality assessment by quantifying the key characteristics of the development process, including efficiency and maintainability. A review of the literature reveals that commonly reported metrics include structural complexity measures, which assess software architecture using indicators such as the number of modules and interconnections [23]. Quality metrics are used to forecast software reliability and support decision-making throughout the SDLC [24]. Finally, productivity metrics are reported, and these assess the impact of GAI-based tools on development speed, quality, and overall efficiency [6], [25]. (Generative Artificial Intelligence for Software Development Using ISO/IEC 29110 Basic Profile: Gaps and Opportunities, page 2)

4. Metrics and roles play a fundamental role in SD, as supported by GAI. The utilization of these metrics enables the establishment of an objective for evaluating the quality of AI-generated codes, including their accuracy and efficiency. These measures empower developers to evaluate the congruence between the resulting artifacts and original objectives, thereby identifying opportunities for enhancement [21], [22]. More broadly, metrics support software engineering quality assessment by quantifying the key characteristics of the development process, including efficiency and maintainability. A review of the literature reveals that commonly reported metrics include structural complexity measures, which assess software architecture using indicators such as the number of modules and interconnections [23]. Quality metrics are used to forecast software reliability and support decision-making throughout the SDLC [24]. Finally, productivity metrics are reported, and these assess the impact of GAI-based tools on development speed, quality, and overall efficiency [6], [25]. (Generative Artificial Intelligence for Software Development Using ISO/IEC 29110 Basic Profile: Gaps and Opportunities, page 2)

5. Software testing plays an essential role in Software Development Life Cycle (SDLC) as it ensures the quality and correctness of the software system. However, complete testing of a software system is practically not possible as it consumes an enormous amount of time and resources [1], [2]. Furthermore, faults are normally not distributed uniformly across software modules. Therefore, it is mostly inefficient or impossible to spend the same amount of testing resources and efforts on every individual software module of the system under test. To overcome this problem, Software Fault Prediction (SFP) has been introduced to early identify faulty software modules prior to the testing phase so that the allocation of testing resources can be economically optimised. (Error-Type—A Novel Set of Software Metrics for Software Fault Prediction, page 1)

6. In this study, software metrics have been imported from the BugHunter Dataset and re-validated using Metric-sReloaded [49], which is a tool for obtaining/measuring software metrics from source codes. The software metrics we used in this study are at the class level and can be found in Table 2.

The reasons we employed the BugHunter Dataset are (1) the software metrics were collected from large industrial projects which are still actively maintained; (2) the source codes of the projects are publicly available via GitHub [50] for us to verify the correctness of the collected software metrics and extract the ESM values; and (3) the BugHunter Dataset collects software metrics based on before-fix and after-fix snapshots of the source code elements that were affected by bugs whilst leaving the source code elements that were not affected by bugs untouched. This approach is useful to capture the changes in software metrics when a bug is being fixed. The empirical evaluations showed that the dataset can be used for further investigations such as bug prediction. (Error-Type—A Novel Set of Software Metrics for Software Fault Prediction, page 5)

7. TABLE 2. Frequently Used Metrics in Software Fault Prediction.

Tabel ini memuat beberapa studi terkait penggunaan metrik dalam prediksi kegagalan perangkat lunak. Lima belas penelitian yang disebutkan menunjukkan bahwa beberapa metrik telah digunakan secara luas dalam prediksi kegagalan, seperti metrik yang terkait dengan sifat objek-oriented dan perilaku pengguna.

Variabel utama di tabel ini meliputi nama penulis, judul penelitian, metode yang digunakan, serta hasil yang diperoleh. Nilai penting dari tabel ini adalah penemuan bahwa beberapa metrik khususnya terkait dengan sifat objek-oriented telah terbukti efektif dalam prediksi kegagalan perangkat lunak.

Pola penting dapat dilihat dari kemunculan istilah-istilah seperti "C&K metrics" dan "Li and Henry," yang mengindikasikan bahwa ada metrik yang secara konsisten digunakan dalam penelitian-penelitian ini. Selain itu, juga terlihat bahwa beberapa penulis menggunakan kombinasi berbagai metode analisis untuk mencapai hasil prediksi yang lebih akurat.

Insight singkat dari tabel ini adalah pentingnya penggunaan metrik-metrik tertentu dalam prediksi kegagalan perangkat lunak. Dengan demikian, penelitian ini menunjukkan bahwa dengan memahami dan menggunakan metrik yang tepat, kita dapat meningkatkan akurasi prediksi kegagalan perangkat lunak. (Efficacy of Inheritance Aspect in Software Fault Prediction—A Survey Paper, page 13)

8. TABLE 6. Experimental results.

Penelitian ini menunjukkan bahwa metrik software baru yang disebut Error-Type dapat digunakan untuk memprediksi kegagalan sistem dengan lebih akurat. Dalam eksperimen ini, empat model belajar mesin (machine learning) dipadankan menggunakan dataset SoftWare Metrics dan Full Dataset.

Dari hasil eksperimen, ditemukan bahwa ketika feature selection tidak diaplikasikan, performance model belajar mesin berkurang karena masalah multi-kolinieritas yang menyebabkan pengaruh negatif terhadap hasil akhir. Namun, setelah feature selection diterapkan, masalah ini dapat dihilangkan, sehingga penggunaan metrik ESM yang baru memberikan informasi lebih bermanfaat kepada model belajar mesin.

Dengan demikian, penelitian ini berhasil menunjukkan bahwa penggunaan Error-Type sebagai metrik software baru dapat meningkatkan keakuratan prediksi kegagalan sistem dan meningkatkan performa model belajar mesin. (Error-Type—A Novel Set of Software Metrics for Software Fault Prediction, page 9)

### response

Software metrics membantu software testing dengan memungkinkan pengembang untuk memantau kualitas perangkat lunak dan mengidentifikasi bagian yang paling cenderung mengalami kesalahan. Dengan demikian, tester dapat merencanakan tes berdasarkan bagian yang paling rentan terhadap kerusakan.

### reference


Software metrics make it easy for developers to audit and monitor the quality of software design as the project progresses. In addition, predicting the probability of defective classes is needed to help the software engineers during development to enhance the quality of software and reduce testing and maintenance costs.

Measurement is needed to validate the effectiveness of software development process. The phrase software metrics describes measurements made on an artifact of software whereas a software artifact has two significant elements: the coded implementation, and the document of its design specification.

Metrics and roles play a fundamental role in SD, as supported by GAI. The utilization of these metrics enables the establishment of an objective for evaluating the quality of AI-generated codes, including their accuracy and efficiency.

Software testing plays an essential role in Software Development Life Cycle (SDLC) as it ensures the quality and correctness of the software system. However, complete testing of a software system is practically not possible as it consumes an enormous amount of time and resources [1], [2].

In this study, software metrics have been imported from the BugHunter Dataset and re-validated using Metric-sReloaded [49], which is a tool for obtaining/measuring software metrics from source codes. The software metrics we used in this study are at the class level and can be found in Table 2.

Frequently Used Metrics in Software Fault Prediction. Tabel ini memuat beberapa studi terkait penggunaan metrik dalam prediksi kegagalan perangkat lunak.

TABLE 6. Experimental results.
