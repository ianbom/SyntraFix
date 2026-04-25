# RAGAS Test Data

File ini digenerate dari tabel `chats`, `chat_references`, dan `document_chunks`.
`retrieved_context` memakai `document_chunks.content` jika tersedia, lalu fallback ke `chat_references.quote`.
`reference` sengaja dikosongkan agar dapat diisi manual.

## Sample 11

- conversation_id: 13
- user_chat_id: 501
- bot_chat_id: 502

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

8. Software analytics is defined as ''analytics on software data for managers and software engineers with the aim of empowering software development individuals and teams to gain and share insight from their data to make better decisions'' [6]. In this context, analytics results should include some actionable knowledge that can be used to improve software quality. Software analytics is used in various scenarios to assess concrete problems, e.g., use of process data to predict overall project effort [26], use of security data to identify indicators for software vulnerabilities [27], or classification of app reviews [28]. In this context, software analytics tools provide features for specifically visualizing software development aspects. In our view, some notable examples are SonarQube, 11 Kiuwan, Bitergia, 12 and Tasktop, all of which have been discussed in related work. (Continuously Assessing and Improving Software Quality With Software Analytics Tools: A Case Study, page 1)

### response

* Totalitas dari karakteristik suatu entitas yang terkait dengan kemampuannya untuk memenuhi kebutuhan yang telah ditetapkan dan implisit.
* Kemampuan suatu sistem software untuk memenuhi kombinasi kualitas atribut yang diinginkan (kompleksitas, keandalan, skalabilitas, fungsi, efisiensi, portabilitas, usability, dan maintainability).
* Kapasitas suatu entitas untuk memenuhi kebutuhan eksplisit dan implisit.
* Totalitas dari karakteristik suatu entitas yang terkait dengan kemampuannya untuk memenuhi kebutuhan yang telah ditetapkan dan implisit.

Informasi tersebut tidak ditemukan pada dokumen yang tersedia.

### reference


These attributes include complexity, reliability, scalability, functionality, efficiency, portability, usability, and maintainability, each contributing to the system's overall effectiveness [8], [9]. Similarly, several studies identify functionality, usability, reliability, performance efficiency, and maintainability as the most impactful measures of software quality [14], [41], [43], [45]. On the other hand, other scholars identify usability, reliability, functionality, performance efficiency, portability, and maintainability as important quality measurements [40], [46].

---

## Sample 12

- conversation_id: 13
- user_chat_id: 503
- bot_chat_id: 504

### user_input

Mengapa software quality penting?

### retrieved_context

1. In general, quality is considered as the most vital factor for meeting customer expectations and organizational growth [12], [34], [40]. More specifically, software quality is a critical success factor for software development companies [12], [13], [41]. Software development companies often depend on effective coordination of software development processes and quality management activities (engineering) to attain the desired level of software quality. In addition to effective coordination, software quality is also affected by cost and time constraints [12], [13], [42], [43]. (How Software Quality Mediates the Impact of Intellectual Capital on Commercial Open-Source Software Company Success, page 3)

2. Quality is the most important factor for software development as it mainly defines customer satisfaction that is directly related to the success of a software project. The software process model is used to ensure software quality, represent a variety of task settings, manage project duration, improve the process and range to execute the process understanding, and to appropriate implicit conjecture for all task settings. Several software processes models exist in software albeit with limited scope. Given this viewpoint, this paper presents a new software development life cycle model, ''AZ-Model,'' for software development by introducing new activities during software development life cycle. It overcomes the limitations of traditional models and significantly impacts the production of a quality product in a time-box. This paper also presents a comprehensive comparative study and statistical analyses to examine the significance of AZ-Model for software development. INDEX TERMS Software development model (SDM), project management (PM), AZ-Model, software development life cycle (SDLC), six pointed star model, project management factors. (Improving the Quality of Software Development Process by Introducing a New Methodology–AZ-Model, page 1)

3. The quality of software continues to be a significant challenge in the software industry, and this challenge is more visible in the Small Software Companies (SSCs) to the extent that up to 70 percent of software projects are challenged either due to defects, cost overruns or overshot scheduling related challenges [1]. Although the products produced by the SSCs fail to meet the expected quality, software is still central in influencing human activity. Recent studies indicate that most aspects of society depend on software; moreover, SSCs are responsible for up to 80 percent of software produced on the market. The contribution of SSCs cannot be underestimated since they represent up to 90 percent of software companies in the industry [2]. (Theory on Non-Technical Characteristics Affecting Process Adoption in Small Software Companies: A Grounded Theory Study, page 1)

4. Software quality is the total characteristics of an entity that depends on its capacity to satisfy explicit and implicit VOLUME 10, 2022 needs [34]- [36]. Hence, poor software quality negatively impacts not only customer satisfaction but also software maintainability, economic gains, and human life in the real-world context [12], [34], [37], [38]. Software maintenance is the most expensive activity in the software development process, representing about 75% of the total cost. Investing in maintenance and defect prevention efforts is critical because software defects have a detrimental effect on the proper functioning of the software. For instance, the world economy has lost 1.1 trillion dollars in 2016 because of software defects, and an estimated 4.4 billion people were affected [38]. A recent report by the Consortium for Information and Software Quality puts the total financial damage caused by poor quality software at 2.08 trillion dollars in 2020 in the US alone [39]. (How Software Quality Mediates the Impact of Intellectual Capital on Commercial Open-Source Software Company Success, page 2)

5. The software development activity is a set of procedures that yields software as an outcome. The procedure and standards in the software development have improved over time and practices like CMM (Capability Maturity Model), now CMMI (Capability Maturity Model Integration), is often considered as an industry standard in software development [1]- [3]. Presence of software in computing devices, mobiles, wearable devices and phablets has made software an entity of extreme relevance in running the life's events and the development of software has therefore increased over time. Ebert [4] has identified that the producers and consumers of software applications have increased, software applications have rationally become more customizable to meet requirements of businesses. (Build Software or Buy: A Study on Developing Large Scale Software, page 1)

6. The software development activity is a set of procedures that yields software as an outcome. The procedure and standards in the software development have improved over time and practices like CMM (Capability Maturity Model), now CMMI (Capability Maturity Model Integration), is often considered as an industry standard in software development [1]- [3]. Presence of software in computing devices, mobiles, wearable devices and phablets has made software an entity of extreme relevance in running the life's events and the development of software has therefore increased over time. Ebert [4] has identified that the producers and consumers of software applications have increased, software applications have rationally become more customizable to meet requirements of businesses. (Build Software or Buy: A Study on Developing Large Scale Software, page 1)

7. Quality of a software product is an intransigence factor. For executable software components, quality comes first and foremost. Addressing quality requirements has always been a challenge for the requirement engineering process and software designing phase [77]. To focus functional requirements of the system, a better designing approach integrating architectural perspective is required along with suitable skills, tools, and techniques.

Quality attributes are the backbone for the success of the software artefacts. Traditionally, quality attributes like usability, reliability and other quality requirements are considered later stages of development that itself leads to late identification of flaws [78]. Therefore, software architecture is considered as favourable choice as it focuses on non-functional quality attributes along with functional requirements to make things smoother [78]. (Integration of Software Architecture in Requirements Elicitation for Rapid Software Development, page 8)

8. Software quality is defined by how closely a software system meets a desired combination of quality attributes [6], [7]. These attributes include complexity, reliability, scalability, functionality, efficiency, portability, usability, and maintainability, each contributing to the system's overall effectiveness [8], [9]. These quality attributes reflect the actual characteristics of the implemented system [8].

In AI-based systems, quality attributes are critical in shaping architectural decisions [4]. These systems introduce additional challenges, such as model management, accuracy, robustness, and inference latency [3], which the architectural design process must carefully address. Consequently, selecting an appropriate architectural style ensures that AI-based software systems meet their requirements effectively. (Architectural Styles and Quality Attributes in AI-Based Video Software: A Systematic Literature Review, page 1)

### response

Software quality penting karena:

* Ia memenuhi harapan pelanggan dan mendukung pertumbuhan organisasi.
* Ia merupakan faktor kesuksesan kritis untuk perusahaan pengembangan perangkat lunak.
* Ia terutama menentukan kepuasan pelanggan yang terkait dengan suksesnya proyek software.
* Software quality dapat dipengaruhi oleh biaya dan waktu batas, serta mempengaruhi kemampuan perangkat lunak untuk memenuhi kebutuhan pelanggan.
* Kualitas perangkat lunak juga mempengaruhi pemeliharaan perangkat lunak, kesepakatan ekonomi, dan kehidupan manusia di konteks nyata.

### reference


In general, quality is considered as the most vital factor for meeting customer expectations and organizational growth [12], [34], [40]. More specifically, software quality is a critical success factor for software development companies [12], [13], [41]. Software development companies often depend on effective coordination of software development processes and quality management activities (engineering) to attain the desired level of software quality. In addition to effective coordination, software quality is also affected by cost and time constraints [12], [13], [42], [43]. (How Software Quality Mediates the Impact of Intellectual Capital on Commercial Open-Source Software Company Success, page 3)

---

## Sample 13

- conversation_id: 13
- user_chat_id: 505
- bot_chat_id: 506

### user_input

Apa saja faktor yang mempengaruhi software quality?

### retrieved_context

1. In general, quality is considered as the most vital factor for meeting customer expectations and organizational growth [12], [34], [40]. More specifically, software quality is a critical success factor for software development companies [12], [13], [41]. Software development companies often depend on effective coordination of software development processes and quality management activities (engineering) to attain the desired level of software quality. In addition to effective coordination, software quality is also affected by cost and time constraints [12], [13], [42], [43]. (How Software Quality Mediates the Impact of Intellectual Capital on Commercial Open-Source Software Company Success, page 3)

2. The quality of software continues to be a significant challenge in the software industry, and this challenge is more visible in the Small Software Companies (SSCs) to the extent that up to 70 percent of software projects are challenged either due to defects, cost overruns or overshot scheduling related challenges [1]. Although the products produced by the SSCs fail to meet the expected quality, software is still central in influencing human activity. Recent studies indicate that most aspects of society depend on software; moreover, SSCs are responsible for up to 80 percent of software produced on the market. The contribution of SSCs cannot be underestimated since they represent up to 90 percent of software companies in the industry [2]. (Theory on Non-Technical Characteristics Affecting Process Adoption in Small Software Companies: A Grounded Theory Study, page 1)

3. In order to effectively coordinate and evaluate software quality management efforts, software companies use software quality models [34], [37], [44], [45]. The earliest software quality model was proposed by McCall in 1976. The McCall model was later revised by Boehm and Dromey [41], [44], [46], [47]. Recently developed software quality evaluation models include ISO/IEC 25010 which outlines 8 attributes to be used for software quality assessment. In contrast, the earlier version ISO/IEC 9126 adopts 6 characteristics [44], [45], [48].

Despite being viewed as a useful tool for quality assurance [44], software standards or models lack functionality and practical application owing to the ambiguity involved [37], [47]. Gorla and Lin as cited in [49] propose a software quality assessment model that includes relevance and usefulness (i.e., functionality), usability, maintainability, and reliability attributes. On the other hand, other scholars identify usability, reliability, functionality, performance efficiency, portability, and maintainability as important quality measurements [40], [46]. Similarly, several studies identify functionality, usability, reliability, performance efficiency, and maintainability as the most impactful measures of software quality [14], [41], [43], [45]. Consequently, functionality, usability, performance efficiency, reliability, and maintainability indicators are adopted for the evaluation of software quality in this study. (How Software Quality Mediates the Impact of Intellectual Capital on Commercial Open-Source Software Company Success, page 1)

4. Software quality is defined by how closely a software system meets a desired combination of quality attributes [6], [7]. These attributes include complexity, reliability, scalability, functionality, efficiency, portability, usability, and maintainability, each contributing to the system's overall effectiveness [8], [9]. These quality attributes reflect the actual characteristics of the implemented system [8].

In AI-based systems, quality attributes are critical in shaping architectural decisions [4]. These systems introduce additional challenges, such as model management, accuracy, robustness, and inference latency [3], which the architectural design process must carefully address. Consequently, selecting an appropriate architectural style ensures that AI-based software systems meet their requirements effectively. (Architectural Styles and Quality Attributes in AI-Based Video Software: A Systematic Literature Review, page 1)

5. Software quality is the total characteristics of an entity that depends on its capacity to satisfy explicit and implicit VOLUME 10, 2022 needs [34]- [36]. Hence, poor software quality negatively impacts not only customer satisfaction but also software maintainability, economic gains, and human life in the real-world context [12], [34], [37], [38]. Software maintenance is the most expensive activity in the software development process, representing about 75% of the total cost. Investing in maintenance and defect prevention efforts is critical because software defects have a detrimental effect on the proper functioning of the software. For instance, the world economy has lost 1.1 trillion dollars in 2016 because of software defects, and an estimated 4.4 billion people were affected [38]. A recent report by the Consortium for Information and Software Quality puts the total financial damage caused by poor quality software at 2.08 trillion dollars in 2020 in the US alone [39]. (How Software Quality Mediates the Impact of Intellectual Capital on Commercial Open-Source Software Company Success, page 2)

6. TABLE 4. Path coefficients.

Analisis terbaru mengenai komponen kualitas perangkat lunak (software quality) dalam menengahi dampak modal intelektual (intellectual capital) pada kesuksesan perusahaan swasta open-source software (COSS) telah membawa beberapa temuan penting. Data yang dianalisis menunjukkan bahwa ada hubungan positif signifikan antara kualitas perangkat lunak dan kesuksesan COSS (β = 0,581, T-value = 10,842, P-value = 0,000). Sebenarnya, kualitas perangkat lunak memainkan peran mediasi yang signifikan dalam menengahi hubungan antara modal intelektual dan kesuksesan COSS.

Penelitian ini juga menemukan bahwa ada hubungan positif antara kapital struktural (structural capital) dan kualitas perangkat lunak, serta antara kapital manusia (human capital) dan kualitas perangkat lunak. Dalam beberapa kasus, mediasi efektif kapital manusia pada relasi tersebut terbukti signifikan.

Kemudian, hasil analisis menunjukkan bahwa kualitas perangkat lunak merupakan faktor yang sangat penting dalam mempengaruhi kesuksesan COSS. Dengan demikian, penelitian ini mendukung asumsi-asumsi yang telah diusulkan (H1-H11) mengenai hubungan antara modal intelektual dan kualitas perangkat lunak terhadap kesuksesan COSS.

Dari hasil analisis, dapat disimpulkan bahwa kualitas perangkat lunak merupakan faktor penting dalam menengahi dampak kapital manusia terhadap kesuksesan COSS. Hasil ini dapat dijadikan sebagai rujukan bagi pihak manajemen dan strategis dalam mengembangkan kebijakan yang lebih efektif untuk meningkatkan kinerja perusahaan open-source software mereka. (How Software Quality Mediates the Impact of Intellectual Capital on Commercial Open-Source Software Company Success, page 7)

7. TABLE 1. Examples of actions to improve software quality for the adalah tabel yang menyajikan contoh tindakan untuk meningkatkan kualitas perangkat lunak dengan menggunakan alat analitik perangkat lunak. Tabel ini terdiri dari 38 baris dan memiliki 8 kolom.

Tabel tersebut menjelaskan beberapa indikator strategis yang digunakan untuk mengevaluasi kinerja perangkat lunak, seperti "Blocking" yang merupakan indikator strategis untuk mengidentifikasi potensi masalah dalam proses pengembangan. Dalam tabel ini juga dapat dilihat bahwa ada empat faktor utama yang digunakan untuk menilai kualitas perangkat lunak: Code Smells, Design Issues, Performance, dan Security.

Salah satu contoh kasus yang disajikan dalam tabel adalah "Blocking" files problem yang dialami oleh perusahaan NeverLate. Dalam kasus ini, analis perangkat lunak dapat menggunakan alat analitik untuk mengidentifikasi klas-klas file yang memiliki kualitas rendah dan membutuhkan perbaikan.

Analisis dari tabel menunjukkan bahwa perusahaan yang menggunakan Q-Rapids dapat meningkatkan kualitas perangkat lunak mereka dengan menggunakan data historis dan visualisasi data. Dengan demikian, mereka dapat mengidentifikasi masalah-masalah yang signifikan dan mengambil tindakan untuk memperbaiki kinerja perangkat lunak.

Dalam kesimpulan, tabel ini menunjukkan bahwa penggunaan alat analitik perangkat lunak dapat membantu meningkatkan kualitas perangkat lunak dengan cara yang lebih objektif dan data-driven. (Continuously Assessing and Improving Software Quality With Software Analytics Tools: A Case Study, page 6)

8. Nowadays, a company's ability to innovate is increasingly driven by software. Digital technologies play a key role in The associate editor coordinating the review of this manuscript and approving it for publication was Waldemar W. Koczkodaj. the transformation of many industrial companies [1], especially in sectors like the automotive industry, where software (together with electronics) is responsible for over 90% of all innovations [2], [3]. In this context, software quality makes the difference and is an essential competitive factor for company success. (Continuously Assessing and Improving Software Quality With Software Analytics Tools: A Case Study, page 1)

### response

Berikut adalah jawaban atas pertanyaan user berdasarkan konteks:

Faktor yang mempengaruhi software quality adalah:

• Biaya dan waktu keterbatasan (cost and time constraints) [12], [13], [42], [43]
• Koordinasi efektif dari proses pengembangan perangkat lunak dan kegiatan manajemen kualitas (effective coordination of software development processes and quality management activities)
• Kapital struktural (structural capital) [β = 0,581, T-value = 10,842, P-value = 0,000]
• Kapital manusia (human capital) [β = 0,581, T-value = 10,842, P-value = 0,000]

### reference


Penelitian ini juga menemukan bahwa ada hubungan positif antara kapital struktural (structural capital) dan kualitas perangkat lunak, serta antara kapital manusia (human capital) dan kualitas perangkat lunak. Dari hasil analisis, dapat disimpulkan bahwa kualitas perangkat lunak merupakan faktor penting dalam menengahi dampak kapital manusia terhadap kesuksesan COSS. In addition to effective coordination, software quality is also affected by cost and time constraints [12], [13], [42], [43]. (How Software Quality Mediates the Impact of Intellectual Capital on Commercial Open-Source Software Company Success, page 3)

---

## Sample 14

- conversation_id: 13
- user_chat_id: 507
- bot_chat_id: 508

### user_input

Bagaimana software quality dapat diukur?

### retrieved_context

1. In order to effectively coordinate and evaluate software quality management efforts, software companies use software quality models [34], [37], [44], [45]. The earliest software quality model was proposed by McCall in 1976. The McCall model was later revised by Boehm and Dromey [41], [44], [46], [47]. Recently developed software quality evaluation models include ISO/IEC 25010 which outlines 8 attributes to be used for software quality assessment. In contrast, the earlier version ISO/IEC 9126 adopts 6 characteristics [44], [45], [48].

Despite being viewed as a useful tool for quality assurance [44], software standards or models lack functionality and practical application owing to the ambiguity involved [37], [47]. Gorla and Lin as cited in [49] propose a software quality assessment model that includes relevance and usefulness (i.e., functionality), usability, maintainability, and reliability attributes. On the other hand, other scholars identify usability, reliability, functionality, performance efficiency, portability, and maintainability as important quality measurements [40], [46]. Similarly, several studies identify functionality, usability, reliability, performance efficiency, and maintainability as the most impactful measures of software quality [14], [41], [43], [45]. Consequently, functionality, usability, performance efficiency, reliability, and maintainability indicators are adopted for the evaluation of software quality in this study. (How Software Quality Mediates the Impact of Intellectual Capital on Commercial Open-Source Software Company Success, page 1)

2. Software quality is calculated in the following formula (4):  In formula (4), q is Software quality; b is Open bugs; l is Total changed codes. Software quality is expressed by the bug rate, which is equal to the number of Open bugs divided by the Total changed codes.

In Quality assurance subsystem, Code review by numerous reviewers, particularly when carried out in tandem with automatic test, can significantly, positively impact software quality. Code review in Figure 7 is a ratio of the effectiveness of the review. If it is equal to 0, it means that the changed code is not reviewed. In the following empirical case study (in Section III), we input a random function to analyze its impact. (Change-Oriented Open Source Software Process Simulation, page 1)

3. Software quality is defined by how closely a software system meets a desired combination of quality attributes [6], [7]. These attributes include complexity, reliability, scalability, functionality, efficiency, portability, usability, and maintainability, each contributing to the system's overall effectiveness [8], [9]. These quality attributes reflect the actual characteristics of the implemented system [8].

In AI-based systems, quality attributes are critical in shaping architectural decisions [4]. These systems introduce additional challenges, such as model management, accuracy, robustness, and inference latency [3], which the architectural design process must carefully address. Consequently, selecting an appropriate architectural style ensures that AI-based software systems meet their requirements effectively. (Architectural Styles and Quality Attributes in AI-Based Video Software: A Systematic Literature Review, page 1)

4. Quality is defined by ISO 8042 [18] as ''the totality of characteristics of an entity that bear on its ability to satisfy stated and implied needs''. This definition is too abstract to be operationalized directly, and is one of the reasons why there has been a multitude of software QMs proposed in the last four decades (e.g., [15], [19]- [22]) that refine high-level concepts of ''quality'' (like reliability or efficiency) down to the level of metrics (as number of bugs or response time). One popular example widely adopted in industry is the ISO/IEC 25010 standard [14], which determines the quality aspects to be taken into account when evaluating the properties of a software product. Two more recent examples well known in industry are Quamoco and SQALE [23]. Quamoco [16] is a QM integrating abstract quality aspects and concrete quality measurements. SQALE [24] computes technical debt indexes based on the violations of quality rules in the source code. Other works propose refactoring models to improve a particular quality aspect of the existing model or code, and different extensions to the traditional concept of quality (such as incorporation of non-technical criteria into ISO/IEC 9126-1 QM [25]). (Continuously Assessing and Improving Software Quality With Software Analytics Tools: A Case Study, page 1)

5. Quality is defined by ISO 8042 [18] as ''the totality of characteristics of an entity that bear on its ability to satisfy stated and implied needs''. This definition is too abstract to be operationalized directly, and is one of the reasons why there has been a multitude of software QMs proposed in the last four decades (e.g., [15], [19]- [22]) that refine high-level concepts of ''quality'' (like reliability or efficiency) down to the level of metrics (as number of bugs or response time). One popular example widely adopted in industry is the ISO/IEC 25010 standard [14], which determines the quality aspects to be taken into account when evaluating the properties of a software product. Two more recent examples well known in industry are Quamoco and SQALE [23]. Quamoco [16] is a QM integrating abstract quality aspects and concrete quality measurements. SQALE [24] computes technical debt indexes based on the violations of quality rules in the source code. Other works propose refactoring models to improve a particular quality aspect of the existing model or code, and different extensions to the traditional concept of quality (such as incorporation of non-technical criteria into ISO/IEC 9126-1 QM [25]). (Continuously Assessing and Improving Software Quality With Software Analytics Tools: A Case Study, page 1)

6. In general, quality is considered as the most vital factor for meeting customer expectations and organizational growth [12], [34], [40]. More specifically, software quality is a critical success factor for software development companies [12], [13], [41]. Software development companies often depend on effective coordination of software development processes and quality management activities (engineering) to attain the desired level of software quality. In addition to effective coordination, software quality is also affected by cost and time constraints [12], [13], [42], [43]. (How Software Quality Mediates the Impact of Intellectual Capital on Commercial Open-Source Software Company Success, page 3)

7. Software analytics is defined as ''analytics on software data for managers and software engineers with the aim of empowering software development individuals and teams to gain and share insight from their data to make better decisions'' [6]. In this context, analytics results should include some actionable knowledge that can be used to improve software quality. Software analytics is used in various scenarios to assess concrete problems, e.g., use of process data to predict overall project effort [26], use of security data to identify indicators for software vulnerabilities [27], or classification of app reviews [28]. In this context, software analytics tools provide features for specifically visualizing software development aspects. In our view, some notable examples are SonarQube, 11 Kiuwan, Bitergia, 12 and Tasktop, all of which have been discussed in related work. (Continuously Assessing and Improving Software Quality With Software Analytics Tools: A Case Study, page 1)

8. Software analytics is defined as ''analytics on software data for managers and software engineers with the aim of empowering software development individuals and teams to gain and share insight from their data to make better decisions'' [6]. In this context, analytics results should include some actionable knowledge that can be used to improve software quality. Software analytics is used in various scenarios to assess concrete problems, e.g., use of process data to predict overall project effort [26], use of security data to identify indicators for software vulnerabilities [27], or classification of app reviews [28]. In this context, software analytics tools provide features for specifically visualizing software development aspects. In our view, some notable examples are SonarQube, 11 Kiuwan, Bitergia, 12 and Tasktop, all of which have been discussed in related work. (Continuously Assessing and Improving Software Quality With Software Analytics Tools: A Case Study, page 1)

### response

Berikut adalah beberapa cara untuk mengukur software quality berdasarkan konteks yang disediakan:

* Dengan menggunakan formula (4): q = b / l, di mana q adalah Software quality, b adalah Open bugs, dan l adalah Total changed codes.
* Dengan memperhitungkan atribut-atribut kualitas seperti kompleksitas, keandalan, skala, fungsi, efisiensi, portabilitas, kemanfaatan, dan perawatan (maintainability).
* Dengan menggunakan standar ISO/IEC 25010 yang memiliki 8 atribut untuk mengevaluasi kualitas software.
* Dengan membandingkan hasil analisis data dengan standar kinerja yang ditetapkan.
* Dengan menggunakan alat-alat analytics seperti SonarQube, Kiuwan, Bitergia, dan Tasktop untuk mengukur kualitas software.

Informasi tersebut tidak ditemukan pada dokumen yang tersedia.

### reference


Software quality is calculated in the following formula (4): In formula (4), q is Software quality; b is Open bugs; l is Total changed codes. Software quality is expressed by the bug rate, which is equal to the number of Open bugs divided by the Total changed codes. In our view, some notable examples are SonarQube, 11 Kiuwan, Bitergia, 12 and Tasktop, all of which have been discussed in related work. (Continuously Assessing and Improving Software Quality With Software Analytics Tools: A Case Study, page 1)

---

## Sample 15

- conversation_id: 13
- user_chat_id: 509
- bot_chat_id: 510

### user_input

Apa hubungan software quality dengan software testing?

### retrieved_context

1. Software testing covers several activities of the software development processes starting from the validation of initial requirements through to the acceptance of the end product by the customer [9]. Starting from the requirement specifications, the software testing tasks need to be planned and implemented in different stages of the software development process. Furthermore, software testing needs to be performed during different stages of the software development process for different purposes, such as the testing of the software product lines [10] and the graphical user interface [11]. (Evolution of Software Testing Strategies and Trends: Semantic Content Analysis of Software Research Corpus of the Last 40 Years, page 2)

2. Testing is defined as ''an activity in which a system is executed under specified conditions, the results are observed or recorded, and an evaluation is made of some aspect of the system'' (ISO/IEC 24765, 2006) [6]. In parallel to this definition of testing, a major task of the software development process, software testing is defined as the process of observing and demonstrating the behavior of a software system for compliance with its specifications [7]. As it requires several strategies and techniques with the involvement of several tools and resources, software testing is also considered as a complex task [8]. The background for this study is given below, summarizing the important role of software testing in the software development life cycle, potential impact of software testing strategies, and review studies conducted on software testing. (Evolution of Software Testing Strategies and Trends: Semantic Content Analysis of Software Research Corpus of the Last 40 Years, page 1)

3. An analysis of the whole software development process reveals that the testing stage has the longest duration and is the most expensive phase [17] involving labor-intensive tasks [18]. As the software testing process is usually performed with limited resources under time constraints, currently, several research studies are being conducted to improve software testing techniques in order to obtain higher-quality and more reliable software products [19]. (Evolution of Software Testing Strategies and Trends: Semantic Content Analysis of Software Research Corpus of the Last 40 Years, page 2)

4. Quality is defined by ISO 8042 [18] as ''the totality of characteristics of an entity that bear on its ability to satisfy stated and implied needs''. This definition is too abstract to be operationalized directly, and is one of the reasons why there has been a multitude of software QMs proposed in the last four decades (e.g., [15], [19]- [22]) that refine high-level concepts of ''quality'' (like reliability or efficiency) down to the level of metrics (as number of bugs or response time). One popular example widely adopted in industry is the ISO/IEC 25010 standard [14], which determines the quality aspects to be taken into account when evaluating the properties of a software product. Two more recent examples well known in industry are Quamoco and SQALE [23]. Quamoco [16] is a QM integrating abstract quality aspects and concrete quality measurements. SQALE [24] computes technical debt indexes based on the violations of quality rules in the source code. Other works propose refactoring models to improve a particular quality aspect of the existing model or code, and different extensions to the traditional concept of quality (such as incorporation of non-technical criteria into ISO/IEC 9126-1 QM [25]). (Continuously Assessing and Improving Software Quality With Software Analytics Tools: A Case Study, page 1)

5. Quality is defined by ISO 8042 [18] as ''the totality of characteristics of an entity that bear on its ability to satisfy stated and implied needs''. This definition is too abstract to be operationalized directly, and is one of the reasons why there has been a multitude of software QMs proposed in the last four decades (e.g., [15], [19]- [22]) that refine high-level concepts of ''quality'' (like reliability or efficiency) down to the level of metrics (as number of bugs or response time). One popular example widely adopted in industry is the ISO/IEC 25010 standard [14], which determines the quality aspects to be taken into account when evaluating the properties of a software product. Two more recent examples well known in industry are Quamoco and SQALE [23]. Quamoco [16] is a QM integrating abstract quality aspects and concrete quality measurements. SQALE [24] computes technical debt indexes based on the violations of quality rules in the source code. Other works propose refactoring models to improve a particular quality aspect of the existing model or code, and different extensions to the traditional concept of quality (such as incorporation of non-technical criteria into ISO/IEC 9126-1 QM [25]). (Continuously Assessing and Improving Software Quality With Software Analytics Tools: A Case Study, page 1)

6. Barmi et al. conducted a systematic review to better understand the connections between the specifications and testing requirements and reported that ''Model-based testing'' was the most commonly studied topic (26%), followed by ''Formal Approaches'' (24%), and ''Traceability'' (18%) and concluded that there was a significant gap between the specification and testing requirements [31]. Their study is considering the relationship between the specifications and testing requirements, not the whole process of software testing. In this context, Garousi and Mäntylä reported that over 101 secondary research studies (as a study of studies) had been published in the area of software testing since 1994, with model-based software testing being the most popular method, web-services the most popular system, and regression testing the most popular testing phase [32]. Since this was a ternary study, it has limitations in showing the whole picture of the software testing studies. Zein et al. performed a systematic mapping study in order to reveal testing techniques for mobile application and mapped 79 empirical studies to a taxonomy [33]. (Evolution of Software Testing Strategies and Trends: Semantic Content Analysis of Software Research Corpus of the Last 40 Years, page 1)

7. In the software testing stages, the aim is to develop softwareoriented products and services in a systematic and efficient manner, in which a wide range of tasks, methods, and strategies are used. Depending on the type, scope and context of the designed and developed, the methods and strategies  chosen during the software testing stages vary considerably. The findings of this study offer a wide-ranging insight into not only the themes and trends in focus but also the tools, tasks, methods, and strategies specific to software testing. Specifically, the discovered topics reveal that the most focused tasks in software testing are specification, transformation, detection, localization, generation, evaluation, optimization, verification, and prediction. The important background provided by the core tasks highlighted in this study for software testing has also been addressed by previous studies [49]. (Evolution of Software Testing Strategies and Trends: Semantic Content Analysis of Software Research Corpus of the Last 40 Years, page 9)

8. ''Testing AI software refers to diverse testing activities for AI-based software/systems. Well-defined quality validation models, methods, techniques, and tools must be developed and applied for AI-based software to facilitate the test activities to achieve well-defined test requirements and meet pre-selected adequate testing criteria and quality assurance standards.'' Therefore, testing AI features of the software includes different testing activities to find software errors, verify the performance of software, and assuring quality validation methods need to be developed. The testing goal is to achieve well-defined test requirements, meet pre-defined testing criteria, and standards of quality assurance of the under-test AI software. (Testing and Quality Validation for AI Software–Perspectives, Issues, and Practices, page 1)

### response

Informasi tersebut tidak ditemukan pada dokumen yang tersedia.

### reference


Software testing covers several activities of the software development processes starting from the validation of initial requirements through to the acceptance of the end product by the customer [9]. Starting from the requirement specifications, the software testing tasks need to be planned and implemented in different stages of the software development process. Furthermore, software testing needs to be performed during different stages of the software development process for different purposes, such as the testing of the software product lines [10] and the graphical user interface [11]. (Evolution of Software Testing Strategies and Trends: Semantic Content Analysis of Software Research Corpus of the Last 40 Years, page 2)
