---
title: "Medizinische Zwangsbehandlung und Zwangsmedikation"
date: 2026-10-25
lastmod: 2026-10-25
description: "Voraussetzungen, Verfahren und Rechtsschutz bei medizinischer Behandlung gegen den Willen der betroffenen Person: Behandlung ohne Zustimmung während der fürsorgerischen Unterbringung (Art. 433–439 ZGB), Notfallbehandlung, Zwangsmedikation im strafrechtlichen Massnahmenvollzug (Art. 59 StGB) und Zwangsernährung; grundrechtliche Anforderungen nach Art. 10 Abs. 2 und Art. 36 BV."
tags: ["Zwangsbehandlung", "Zwangsmedikation", "Behandlung ohne Zustimmung", "Fürsorgerische Unterbringung", "Behandlungsplan", "Urteilsunfähigkeit", "Depotmedikation", "Zwangsernährung", "Massnahmenvollzug", "Persönliche Freiheit"]
typ: verfahren
kurz: "Eine medizinische Behandlung gegen den Willen einer Person ist ein schwerer Eingriff in die persönliche Freiheit und nur unter engen Voraussetzungen zulässig. Während einer fürsorgerischen Unterbringung darf die Chefärztin oder der Chefarzt eine psychiatrische Behandlung nach Behandlungsplan schriftlich anordnen, wenn ohne sie ein ernsthafter Gesundheitsschaden oder eine ernsthafte Gefahr für Dritte droht, die Person ihre Behandlungsbedürftigkeit nicht beurteilen kann und kein milderes Mittel genügt; dagegen kann innert zehn Tagen das Gericht angerufen werden. Im strafrechtlichen Massnahmenvollzug entscheidet die Vollzugsbehörde gestützt auf Art. 59 StGB und das kantonale Vollzugsrecht."
sachgebiete: [familienrecht.fu, familienrecht.erwachsenenschutz, strafvollzug, strafrecht.massnahmen, grundrechte]
normen:
  - { gesetz: zgb, art: art-377 }
  - { gesetz: zgb, art: art-380 }
  - { gesetz: zgb, art: art-426 }
  - { gesetz: zgb, art: art-433 }
  - { gesetz: zgb, art: art-434 }
  - { gesetz: zgb, art: art-435 }
  - { gesetz: zgb, art: art-438 }
  - { gesetz: zgb, art: art-439 }
  - { gesetz: zgb, art: art-450e }
  - { gesetz: stgb, art: art-059 }
  - { gesetz: bv, art: art-010 }
  - { gesetz: bv, art: art-036 }
  - { gesetz: emrk, art: art-003 }
  - { gesetz: emrk, art: art-008 }
stichworte: ["Zwangsmedikation", "Zwangsbehandlung", "Behandlung ohne Zustimmung", "Behandlungsplan", "Depotmedikation", "Neuroleptika", "Zwangsernährung", "Hungerstreik", "Anorexie", "Patientenverfügung", "Notfallbehandlung", "Chefarzt", "FU-Gericht"]
revisions:
  - date: 2026-10-25
    by: "Claude Code"
    model: "claude-opus-5-5"
    note: "Erstfassung nach Skill glossagens-themen (Typ verfahren, Querschnitt ZGB/StGB/BV). Normtexte Art. 434 und 435 ZGB per scripts/wortlaut.py (Fedlex, Stand 01.07.2026); Art. 377, 380, 433, 438, 439, 450e ZGB und Art. 59 StGB über die Fedlex-MCP geprüft. Entscheide als Volltext über entscheidsuche.ch geladen (MCP nicht erreichbar, Suche über den Elasticsearch-Proxy): BGE 125 III 169, 126 I 112, 127 I 6, 127 IV 154, 130 I 16, 130 IV 49, 134 I 221, 136 IV 97, 143 III 337; BGer 5A_985/2020, 5A_1021/2021, 5A_857/2024, 5A_122/2026, 6B_554/2021, 7B_124/2026. BGE 134 I 221 und 136 IV 97 liegen nur französisch vor, die Darstellung stützt sich auf die deutsche Regeste. Zitate und Links mit pruefen.py geprüft. agent_verified bewusst false (inhaltliche Durchsicht durch Maintainer)."
---

## Überblick {#ueberblick}

Wer urteilsfähig ist, entscheidet selbst, ob er sich behandeln lässt — auch dann, wenn die Ablehnung medizinisch unvernünftig ist. Eine Behandlung gegen den Willen der betroffenen Person ist deshalb die Ausnahme und bedarf einer besonderen Rechtfertigung. Das Bundesgericht hält fest, dass eine medikamentöse Zwangsbehandlung «einen schweren Eingriff in die persönliche Freiheit im Sinne der körperlichen und geistigen Integrität nach Art. 10 Abs. 2 BV und Art. 8 Ziff. 1 EMRK darstellt und die Menschenwürde gemäss Art. 7 BV zentral betrifft» ([BGE 130 I 16](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_001_BGE-130-I-16_2004.html#consideration_3.) E. 3). Ein solcher Eingriff braucht nach Art. 36 BV eine klare formellgesetzliche Grundlage, ein überwiegendes Interesse und muss verhältnismässig sein.

Die Rechtsordnung kennt dafür zwei Hauptwege, die sich nach Zweck, Zuständigkeit und Rechtsweg unterscheiden:

| | Erwachsenenschutz (Zivilrecht) | Strafrechtlicher Massnahmenvollzug |
|---|---|---|
| Lage der Person | fürsorgerisch untergebracht ([Art. 426 ZGB](/kommentar/zgb/art-426/)) | stationäre therapeutische Massnahme ([Art. 59 StGB](/kommentar/stgb/art-059/)) |
| Zweck | Schutz der Person vor ernsthaftem Gesundheitsschaden, Schutz Dritter | Erreichen des Massnahmenzwecks, Verbesserung der Legalprognose |
| Rechtsgrundlage | Art. 433–435 ZGB (seit 1.1.2013) | Art. 59 StGB i.V.m. kantonalem Justizvollzugsrecht |
| Anordnung | Chefärztin oder Chefarzt der Abteilung | Vollzugsbehörde |
| Rechtsschutz | Anrufung des Gerichts innert 10 Tagen (Art. 439 ZGB), danach Beschwerde in Zivilsachen | kantonaler Rechtsmittelweg, danach Beschwerde in Strafsachen |

Daneben stehen die **Notfallbehandlung** (Art. 435 ZGB) und Sonderlagen wie die **Zwangsernährung** im Strafvollzug. Dieses Thema stellt die beiden Hauptwege in ihrem Ablauf dar und verweist für die Unterbringung selbst auf den Kommentar zu [Art. 426 ZGB](/kommentar/zgb/art-426/).

### Rechtslage vor 2013 {#rechtslage-vor-2013}

Das frühere Vormundschaftsrecht regelte nur den fürsorgerischen Freiheitsentzug, nicht die Behandlung in der Anstalt. Das Bundesgericht entschied deshalb, die Bestimmungen über die fürsorgerische Freiheitsentziehung böten keine Grundlage für eine Behandlung gegen den Willen: «Die Art. 397a ff. ZGB bieten für eine Zwangsbehandlung zu therapeutischen Zwecken keine Gesetzesgrundlage» ([BGE 125 III 169](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_005_BGE-125-III-169_1999-04-29.html), Regeste). Massgebend waren damit die kantonalen Psychiatrie- und Gesundheitsgesetze, an denen das Bundesgericht die grundrechtlichen Anforderungen entwickelte ([BGE 126 I 112](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_001_BGE-126-I-112_2000-05-23.html); [BGE 127 I 6](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_001_BGE-127-I-6_2001-03-22.html) zum Basler Psychiatriegesetz; BGE 130 I 16 zum Zuger Gesundheitsgesetz). Diese Rechtsprechung ist für die Auslegung des heutigen Rechts, namentlich die Verhältnismässigkeit, weiterhin der Ausgangspunkt.

---

## Ablauf im Erwachsenenschutz {#ablauf-erwachsenenschutz}

| Phase | Zuständig | Frist / Form | Rechtsbehelf |
|---|---|---|---|
| 1. Unterbringung zur Behandlung einer psychischen Störung | KESB oder, nach kantonalem Recht, Ärztin/Arzt (Art. 426 ff. ZGB) | Entscheid | Anrufung des Gerichts bzw. Beschwerde |
| 2. Behandlungsplan | behandelnde Ärztin/behandelnder Arzt (Art. 433 ZGB) | schriftlich, unter Beizug der Person | — (Zustimmung oder Ablehnung) |
| 3. Anordnung der Behandlung ohne Zustimmung | Chefärztin/Chefarzt der Abteilung (Art. 434 ZGB) | schriftlich, mit Rechtsmittelbelehrung | Anrufung des Gerichts innert 10 Tagen (Art. 439 Abs. 1 Ziff. 4, Abs. 2 ZGB) |
| 4. Vollzug | Klinikpersonal | nach der Anordnung | gerichtliche Überprüfung auch als Realakt |
| 5. Gerichtliche Überprüfung | kantonales Gericht | Entscheid auf Gutachten (Art. 450e Abs. 3 ZGB), in der Regel innert fünf Arbeitstagen (Art. 450e Abs. 5 ZGB) | Beschwerde in Zivilsachen ans Bundesgericht |
| Notfall | Einrichtung (Art. 435 ZGB) | sofort | nachträgliche Überprüfung |

### Anwendungsbereich {#anwendungsbereich}

Art. 433–435 ZGB stehen im Abschnitt über die fürsorgerische Unterbringung unter der Überschrift *Medizinische Massnahmen bei einer psychischen Störung*. Sie setzen zweierlei voraus: Die Person ist **zur Behandlung einer psychischen Störung untergebracht**, und die Massnahme dient der Behandlung **dieser** Störung. Wird eine urteilsunfähige Person in einer psychiatrischen Klinik wegen einer psychischen Störung behandelt, verweist Art. 380 ZGB auch ausserhalb einer behördlich angeordneten Unterbringung auf diese Bestimmungen. Für andere medizinische Massnahmen bei urteilsunfähigen Personen gilt das Vertretungsrecht nach Art. 377 ff. ZGB (Behandlungsplan unter Beizug der vertretungsberechtigten Person); einen Zwangstatbestand enthält es nicht.

Unter Art. 434 ZGB kann auch eine Zwangsernährung fallen, wenn sie der Behandlung der psychischen Störung dient: Im Fall einer jungen Frau mit chronischer Anorexia nervosa und lebensbedrohlich tiefem Körpergewicht bestätigte das Bundesgericht eine zwölfwöchige Ernährung über eine Sonde gestützt auf Art. 434 ZGB ([BGer 5A_1021/2021](https://entscheidsuche.ch/docs/CH_BGer/CH_BGer_005_5A-1021-2021_2021-12-17.html) E. 5).

### Behandlungsplan (Art. 433 ZGB) {#behandlungsplan}

Grundlage jeder Behandlung — mit und ohne Zustimmung — ist der schriftliche Behandlungsplan. Ihn erstellt die behandelnde Ärztin oder der behandelnde Arzt unter Beizug der betroffenen Person und gegebenenfalls ihrer Vertrauensperson; sie werden über Gründe, Zweck, Art, Modalitäten, Risiken und Nebenwirkungen, die Folgen eines Unterlassens und Behandlungsalternativen informiert (Art. 433 Abs. 1 und 2 ZGB). Der Plan wird der Person zur Zustimmung unterbreitet; bei Urteilsunfähigkeit ist eine allfällige Patientenverfügung zu berücksichtigen (Art. 433 Abs. 3 ZGB). Er wird der laufenden Entwicklung angepasst (Abs. 4).

Der Plan begrenzt zugleich, was ohne Zustimmung angeordnet werden darf: Mit der Anordnung sind «von Gesetzes wegen die im Behandlungsplan vorgesehenen medizinischen Massnahmen gemeint»; «Für eine andere Massnahme ist die Anordnung von Art. 434 ZGB von Gesetzes wegen nicht vorgesehen» ([BGE 143 III 337](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_005_BGE-143-III-337_2017.html#consideration_2.4.2) E. 2.4.2). Eine Änderung der Medikation erfordert deshalb eine Anpassung des Plans.

### Voraussetzungen der Behandlung ohne Zustimmung (Art. 434 ZGB) {#voraussetzungen-art-434}

{{< wortlaut gesetz="zgb" art="art-434" >}}

Die drei Voraussetzungen müssen **kumulativ** erfüllt sein:

**1. Ernsthafte Gefährdung (Ziff. 1).** Entweder droht der Person ohne Behandlung ein ernsthafter gesundheitlicher Schaden, oder das Leben oder die körperliche Integrität Dritter ist ernsthaft gefährdet. «Ernsthaft ist ein Gesundheitsschaden, wenn er zu einer langen Beeinträchtigung wichtiger körperlicher oder psychischer Funktionen führt»; bleibend oder irreversibel muss er nicht sein ([BGer 5A_857/2024](https://entscheidsuche.ch/docs/CH_BGer/CH_BGer_005_5A-857-2024_2025-01-16.html) E. 3.3.1). Eine Lebens- oder Suizidgefahr ist nicht erforderlich (5A_857/2024 E. 3.3.4.1). Das Bundesgericht liess dort das ausserordentlich hohe Risiko einer erneuten psychotischen Dekompensation mit fortschreitender Chronifizierung, Verwahrlosung und grossem Leidensdruck genügen. Ebenso wenig verlangt Art. 434 ZGB eine akute Lebensgefahr: «Die von der Beschwerdeführerin geltend gemachte Bedingung (drohende und akute Lebensgefahr) findet keine Grundlage im Gesetz» (5A_1021/2021 E. 5.3.2). Aus der früheren Rechtsprechung bleibt die Anforderung, dass die Gefährdung konkret belegt sein muss; die zentral betroffenen Verfassungsrechte verlangen, «dass die Selbst- und Fremdgefährdung nicht nur abstrakt möglich sind, sondern gestützt auf die tatsächlichen Verhältnisse konkret in Betracht fallen und als wahrscheinlich erscheinen» (BGE 130 I 16 E. 5.3).

**2. Urteilsunfähigkeit bezüglich der Behandlungsbedürftigkeit (Ziff. 2).** Massgebend ist nicht die Urteilsfähigkeit allgemein, sondern die Fähigkeit, die eigene Krankheit und die Notwendigkeit der Behandlung zu erkennen. Das Bundesgericht bestätigte die Urteilsunfähigkeit einer Frau, die die Medikation zwar klar ablehnen konnte, aber krankheitsbedingt keinen Zusammenhang zwischen Behandlung und Besserung zu erkennen vermochte und Verbesserungen teilweise einem «Heiler» zuschrieb (5A_857/2024 E. 3.4). Die Unterscheidung ist entscheidend: Gegenüber einer **urteilsfähigen** Person, die die Behandlung ablehnt, ist Art. 434 ZGB nicht anwendbar. «Während Urteilsfähige letztlich allein über ihr Leben entscheiden können», steht der Staat gegenüber Urteilsunfähigen in einer Schutzpflicht (5A_1021/2021 E. 5.6.2).

**3. Subsidiarität (Ziff. 3).** Es darf keine angemessene, weniger einschneidende Massnahme zur Verfügung stehen. Die Prüfung folgt dem allgemeinen Verhältnismässigkeitsgrundsatz (Art. 389 Abs. 2 ZGB) mit den Elementen Eignung, Erforderlichkeit und Zumutbarkeit (5A_857/2024 E. 3.5.1; 5A_1021/2021 E. 5.1). Dazu ausführlich unten → [Verhältnismässigkeit](#verhaeltnismaessigkeit).

### Anordnung und Mitteilung {#anordnung}

Zuständig ist nach dem Wortlaut die Chefärztin oder der Chefarzt der Abteilung. Der Entscheid «darf […] auch von einer leitenden Ärztin bzw. von einem leitenden Arzt stellvertretend getroffen werden»; im beurteilten Fall genügte die Unterschrift eines Oberarztes (BGE 143 III 337 E. 2.4.2). Die Anordnung ergeht schriftlich und wird der Person und ihrer Vertrauensperson mit Rechtsmittelbelehrung mitgeteilt (Art. 434 Abs. 2 ZGB).

Aus BGE 143 III 337 ergeben sich drei Grundsätze zur Form:

- Die Verfügung muss die Medikamente nicht selbst nennen; ihr Inhalt ergibt sich aus dem Behandlungsplan (E. 2.4.2).
- Eine länger dauernde Behandlung kann mit **einem** Entscheid angeordnet werden: «Die Behandlung stellt ein Ganzes dar» (E. 2.4.3). Die Verhältnismässigkeit verlangt aber eine zeitliche Begrenzung — im Anorexie-Fall präzisierte das Kantonsgericht die Anordnung auf das Erreichen des Zielgewichts, längstens zwölf Wochen (5A_1021/2021 E. 5.4.1).
- Anordnung und Vollstreckung sind zu unterscheiden: «Die Frage der Anordnung der Behandlung ohne Zustimmung ist mit anderen Worten von jener der Vollstreckung der Anordnung zu unterscheiden» (E. 2.4). Nimmt die Person die Medikamente unter dem Druck der Anordnung *freiwillig*, bleibt die Anordnung anfechtbar.

### Vollzug und begleitende Massnahmen {#vollzug}

«Mit der Anordnung der Behandlung ohne Zustimmung der betroffenen Person ist diese verpflichtet, sie zu dulden»; vorbehältlich einer anderen Anordnung ist das Klinikpersonal ermächtigt, die zur Durchsetzung erforderlichen Zwangsmassnahmen zu treffen (BGE 143 III 337 E. 2.5; die Frage ist in der Lehre umstritten, das Bundesgericht referiert dort die Gegenmeinung). Auch ohne schriftliche Verfügung liegt in einer faktisch durchgesetzten Behandlung ein Realakt, der der gerichtlichen Überprüfung nach Art. 439 Abs. 1 Ziff. 4 ZGB unterliegt (E. 2.7).

Werden zur Durchsetzung Fixierung oder Isolation eingesetzt, sind das Massnahmen zur Einschränkung der Bewegungsfreiheit (Art. 438 ZGB), gegen die das Gericht jederzeit angerufen werden kann (Art. 439 Abs. 1 Ziff. 5, Abs. 2 Satz 2 ZGB). Sie müssen für sich verhältnismässig sein: Das Bundesgericht hielt fest, dass «eine über 12 Wochen dauernde Fixierung als unverhältnismässig zu betrachten wäre», liess aber eine temporäre Fixierung zum Einlegen und Belassen einer Ernährungssonde zu (5A_1021/2021 E. 5.6.1.2).

### Notfälle (Art. 435 ZGB) {#notfaelle}

{{< wortlaut gesetz="zgb" art="art-435" >}}

Art. 435 ZGB erlaubt nur die **unerlässlichen** Massnahmen in einer Notfallsituation, ohne Behandlungsplan und ohne vorgängige Anordnung nach Art. 434 ZGB. Ist der Wille der Person bekannt — etwa aus einer Patientenverfügung —, wird er berücksichtigt (Abs. 2). Eine längerfristige Behandlung lässt sich nicht auf Art. 435 ZGB stützen; sobald der Notfall vorbei ist, gilt das Verfahren nach Art. 433 f. ZGB. Umgekehrt setzt Art. 434 ZGB, wie gezeigt, keine Notfall- oder akute Lebensgefahr voraus (5A_1021/2021 E. 5.3.2).

### Patientenverfügung {#patientenverfuegung}

Eine Patientenverfügung ist bei urteilsunfähigen Personen zu berücksichtigen (Art. 433 Abs. 3 Satz 2 ZGB); Art. 434 ZGB verdrängt sie nicht. In [BGer 5A_985/2020](https://entscheidsuche.ch/docs/CH_BGer/CH_BGer_005_5A-985-2020_2021-05-26.html) hatte die Klinik einige Tage nach Errichtung einer Patientenverfügung ein darin abgelehntes Medikament ohne Zustimmung angeordnet; dem FU-Gericht lag die Verfügung nicht vor. Das Bundesgericht hielt die Fragen nach der gültigen Errichtung (Urteilsfähigkeit bei Errichtung) und nach der Vereinbarkeit der Anordnung mit der Verfügung für entscheidrelevant und ging im Kostenentscheid davon aus, dass die Beschwerde mutmasslich hätte gutgeheissen werden müssen (E. 4.2). Die Klinik muss eine ihr bekannte Patientenverfügung deshalb in die Akten geben, und das Gericht muss sich mit ihr auseinandersetzen.

### Gerichtliche Überprüfung (Art. 439 ZGB) {#gerichtliche-ueberpruefung}

Die betroffene oder eine ihr nahestehende Person kann bei Behandlung einer psychischen Störung ohne Zustimmung schriftlich das zuständige Gericht anrufen (Art. 439 Abs. 1 Ziff. 4 ZGB), innert zehn Tagen seit Mitteilung des Entscheids (Abs. 2). Das Verfahren richtet sich sinngemäss nach den Bestimmungen über die gerichtliche Beschwerdeinstanz (Abs. 3): Die Eingabe muss nicht begründet werden (Art. 450e Abs. 1 ZGB), bei psychischen Störungen wird gestützt auf ein Gutachten einer sachverständigen Person entschieden (Abs. 3), die Person wird in der Regel vom Kollegium angehört (Abs. 4), und der Entscheid ergeht in der Regel innert fünf Arbeitstagen (Abs. 5). Jedes Begehren ist unverzüglich an das zuständige Gericht weiterzuleiten (Art. 439 Abs. 4 ZGB) — auch eine an die Klinik gerichtete Eingabe.

Das Gericht legt nicht selbst die richtige Therapie fest, sondern prüft die gesetzlichen Voraussetzungen; in erster Linie, ob ein verlässliches Gutachten einer unabhängigen Fachperson vorliegt (so das Kantonsgericht St. Gallen, vom Bundesgericht nicht beanstandet, 5A_1021/2021 E. 5.2.1 und 5.2.3).

**Aufschiebende Wirkung.** Ob die Anrufung des Gerichts die Behandlung aufschiebt, ist in der Praxis nicht einheitlich beantwortet. In 5A_985/2020 E. 2.3.2 führte das Bundesgericht aus, nach Art. 450c ZGB, anwendbar über Art. 439 Abs. 3 ZGB, habe die Beschwerde aufschiebende Wirkung, sofern die verfügende Behörde oder die Beschwerdeinstanz nichts anderes verfüge; «Ab welchem Zeitpunkt eine solche vollstreckt werden darf, richtet sich nach den anwendbaren prozessualen Vorschriften». Das Basler FU-Gericht ging demgegenüber gestützt auf Art. 450e Abs. 2 ZGB — die Beschwerde auf dem Gebiet der fürsorgerischen Unterbringung hat keine aufschiebende Wirkung, sofern nichts anderes verfügt wird — davon aus, der Beschwerde gegen eine Behandlung ohne Zustimmung komme von Gesetzes wegen keine aufschiebende Wirkung zu. Das Bundesgericht trat auf die dagegen gerichtete Beschwerde mangels aktuellen Interesses nicht ein und liess die Frage offen ([BGer 5A_122/2026](https://entscheidsuche.ch/docs/CH_BGer/CH_BGer_005_5A-122-2026_2026-02-24.html) E. 1.2.3–1.2.4).

**Weiterzug und Feststellung.** Gegen den kantonalen Entscheid steht die Beschwerde in Zivilsachen offen (Art. 72 Abs. 2 lit. b Ziff. 6 BGG; 5A_857/2024 E. 1.1). Ist die Behandlung beendet, fehlt meist das aktuelle Interesse; ein Begehren auf Feststellung der Widerrechtlichkeit ist im Beschwerdeverfahren grundsätzlich unzulässig, weil dafür die Verantwortlichkeitsklage nach Art. 454 ZGB zur Verfügung steht (5A_122/2026 E. 1.2.2 und 1.2.5; 5A_985/2020 E. 2.2.2).

---

## Zwangsmedikation im strafrechtlichen Massnahmenvollzug {#massnahmenvollzug}

Wer zu einer stationären therapeutischen Massnahme nach [Art. 59 StGB](/kommentar/stgb/art-059/) verurteilt ist, untersteht nicht dem Regime von Art. 434 ZGB, sondern dem Vollzugsrecht. Die Zwangsmedikation dient hier dem Massnahmenzweck, der Gefahr weiterer Taten zu begegnen.

**Rechtsgrundlage.** Bereits zum alten Recht entschied das Bundesgericht: «Art. 43 StGB ist die gesetzliche Grundlage für die ärztliche Behandlung und besondere Pflege. Dies muss auch für die ärztliche Zwangsbehandlung gelten» ([BGE 127 IV 154](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_006_BGE-127-IV-154_2001-06-15.html#consideration_3.), Regeste). Unter geltendem Recht stützt es die Zwangsmedikation auf das kantonale Justizvollzugsrecht zusammen mit Art. 59 StGB ([BGer 6B_554/2021](https://entscheidsuche.ch/docs/CH_BGer/CH_BGer_006_6B-554-2021_2021-06-25.html) E. 2.4.2 mit Hinweis auf BGE 134 I 221 E. 3.3.2 und BGE 130 IV 49 E. 3.3).

**Zuständigkeit.** «Die Vollzugsbehörden sind für die Anordnung einer Zwangsmedikation zuständig, wenn sie dem Massnahmezweck und der Behandlungsart entspricht, die der Richter im Strafurteil vorgezeichnet hat» ([BGE 130 IV 49](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_006_BGE-130-IV-49_2004.html#consideration_3.), Regeste). In der Praxis stellt die Klinik einen Antrag mit Wirkstoffen und Maximaldosierung, die Vollzugsbehörde ordnet befristet an (in 6B_554/2021 für 30 Tage, E. 2.4.3).

**Verhältnismässigkeit.** Es gelten dieselben grundrechtlichen Massstäbe wie im Zivilrecht: formellgesetzliche Grundlage und eine vollständige Interessenabwägung, die öffentliche Interessen, Notwendigkeit der Behandlung, Folgen einer Nichtbehandlung, Alternativen sowie Selbst- und Fremdgefährdung einschliesst (6B_554/2021 E. 2.3.2, gestützt auf BGE 130 I 16 E. 4 und 5). «In diese Interessenabwägung miteinzubeziehen sind nach der bundesgerichtlichen Rechtsprechung insbesondere auch langfristige Nebenwirkungen einer zwangsweise vorgesehenen Neuroleptika-Behandlung» (6B_554/2021 E. 2.3.2). Zulässig war die Medikation dort, weil ohne sie keine geordnete Psychotherapie beginnen konnte und sich die Legalprognose sonst verschlechtert hätte (E. 2.4.2). Ist die befristete Anordnung abgelaufen und soll erneut behandelt werden, haben die Ärzte «einen neuen Behandlungsplan zu erstellen und dem SMV einen entsprechenden Antrag zu unterbreiten» (E. 2.4.3). Die Einzelunterbringung als Alternative zur Zwangsmedikation prüfte das Bundesgericht in [BGE 134 I 221](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_001_BGE-134-I-221_2008.html#consideration_3.3) E. 3.3 (französisch).

**Rechtsweg.** «Die Anordnung einer Zwangsmedikation während eines strafrechtlichen Massnahmenvollzugs ist ein Entscheid über den Vollzug von Massnahmen im Sinne von Art. 78 Abs. 2 lit. b BGG» (6B_554/2021 E. 1.1). Dagegen ist die Beschwerde in Strafsachen gegeben; ist die befristete Anordnung abgelaufen, verzichtet das Bundesgericht auf das aktuelle Interesse, weil sich die Frage wieder stellen kann und eine rechtzeitige Überprüfung kaum je möglich wäre (E. 1.2). Die Gutachtenwürdigung prüft es nur auf Willkür ([BGer 7B_124/2026](https://entscheidsuche.ch/docs/CH_BGer/CH_BGer_007_7B-124-2026_2026-03-31.html) E. 3.3).

---

## Zwangsernährung bei Hungerstreik {#zwangsernaehrung-hungerstreik}

Von der Zwangsernährung urteilsunfähiger Personen (oben, 5A_1021/2021) zu unterscheiden ist der Hungerstreik eines **urteilsfähigen** Gefangenen. Im Fall Rappaz entschied das Bundesgericht, «unter bestimmten Voraussetzungen kann die Strafvollzugsbehörde die Zwangsernährung anordnen»; eine Unterbrechung des Strafvollzugs nach Art. 92 StGB sei subsidiär, solange keine Anhaltspunkte bestünden, dass einer Gesundheitsgefahr nicht durch Zwangsernährung begegnet werden könne ([BGE 136 IV 97](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_006_BGE-136-IV-97_2010.html#consideration_6.), Regeste, E. 6). Die Erwägungen (französisch) stützen den Eingriff mangels bundesrechtlicher Regelung auf die polizeiliche Generalklausel. Das Bundesgericht betonte später, dass die dort entwickelten Grundsätze — Einschreiten nur bei unmittelbarer Lebensgefahr — für Urteilsunfähige nicht gelten (5A_1021/2021 E. 5.6.2).

---

## Grundrechtlicher Rahmen {#grundrechtlicher-rahmen}

Massstab für alle Wege sind die persönliche Freiheit ([Art. 10 Abs. 2 BV](/kommentar/bv/art-010/), [Art. 8 EMRK](/kommentar/emrk/art-008/)), die Menschenwürde (Art. 7 BV) und das Verbot unmenschlicher oder erniedrigender Behandlung ([Art. 3 EMRK](/kommentar/emrk/art-003/)). Daraus folgen nach [Art. 36 BV](/kommentar/bv/art-036/):

- **Gesetzliche Grundlage** im formellen Gesetz (BGE 130 I 16 E. 3). Im Erwachsenenschutz ist sie seit 2013 mit Art. 434 ZGB bundesrechtlich gegeben, im Massnahmenvollzug mit Art. 59 StGB und dem kantonalen Vollzugsrecht.
- **Öffentliches Interesse.** Dem Gemeinwesen kann das Schicksal kranker Personen nicht gleichgültig sein; «Wie weit dieses konkret reicht und wo die Grenze zwischen Selbstbestimmung und staatlicher Fürsorge verläuft, ist vor dem Hintergrund einer umfassenden Interessenabwägung und in Anbetracht der Notwendigkeit der Behandlung zu beurteilen» (BGE 130 I 16 E. 5.2).
- **Verhältnismässigkeit** → nächster Abschnitt.

### Verhältnismässigkeit {#verhaeltnismaessigkeit}

Die Rechtsprechung verlangt eine **umfassende Interessenabwägung** und hat sie in BGE 130 I 16 E. 5.3 aufgefächert. Daraus und aus der neueren Praxis ergibt sich folgendes Prüfraster:

| Element | Was festzustellen ist | Beleg |
|---|---|---|
| Eignung | Spricht die Person auf das Mittel an? Ist das Behandlungsziel erreichbar? | 5A_857/2024 E. 3.5.2; 5A_1021/2021 E. 5.2 |
| Konkrete Gefährdung | Welche Folgen hätte das Absetzen — konkret, nicht abstrakt (*psychotische Dekompensation* genügt als Schlagwort nicht) | BGE 130 I 16 E. 5.3 |
| Alternativen | schwächere oder andere Medikamente, orale statt Depotmedikation, pflegerische Massnahmen (Isolation) | BGE 130 I 16 E. 5.3; 5A_857/2024 E. 3.5.3 |
| Nebenwirkungen | kurz- und langfristige, konkret für die Person | BGE 130 I 16 E. 5.3; 6B_554/2021 E. 2.3.2 |
| Dauer | Befristung, Ziel, Überprüfung | 5A_1021/2021 E. 5.4; 6B_554/2021 E. 2.4.3 |
| Zumutbarkeit | Ängste und Belastung der Person gegen den Nutzen | 5A_857/2024 E. 3.5.4 |

Zwei Fälle zeigen die Spannweite. In BGE 130 I 16 hob das Bundesgericht eine Depotmedikation auf, weil das kantonale Gericht die Folgen eines Absetzens nur abstrakt beschrieben, die Nebenwirkungen (Augenbrennen, hormonelle Störungen) kaum gewürdigt und die Alternative einer schwächeren oralen Medikation, die die Patientin akzeptiert hätte, nicht geprüft hatte (E. 5.3 und 5.4). In 5A_857/2024 hielt es eine Depotmedikation dagegen für erforderlich, weil die Patientin die orale Medikation in einer langen Krankengeschichte immer wieder kurz nach der Entlassung abgesetzt hatte und rasch dekompensierte (E. 3.5.3).

---

## Praxishinweise {#praxishinweise}

**Für Betroffene und ihre Vertretung**
- Die Frist von **zehn Tagen** läuft ab schriftlicher Mitteilung der Anordnung. Eine Begründung ist nicht nötig; eine an die Klinik gerichtete Eingabe muss weitergeleitet werden (Art. 439 Abs. 4 ZGB).
- Sofort ein **Gesuch um aufschiebende Wirkung** stellen — die Praxis ist uneinheitlich (oben → [Aufschiebende Wirkung](#gerichtliche-ueberpruefung)), und ohne Gesuch wird regelmässig sofort behandelt.
- Konkret rügen: welches mildere Mittel (orale statt Depotmedikation, anderes Präparat), welche Nebenwirkungen, warum die Gefährdung nur abstrakt sei. Pauschale Kritik am Gutachten scheitert vor Bundesgericht regelmässig an den Rügeanforderungen (5A_857/2024 E. 3.3.4.1 und 3.4.2; 7B_124/2026 E. 3.5).
- Eine **Patientenverfügung** in die Akten bringen; das Gericht muss sie prüfen (5A_985/2020 E. 4.2).
- Feststellung der Rechtswidrigkeit einer beendeten Behandlung nicht im Beschwerdeverfahren, sondern mit der Klage nach Art. 454 ZGB verlangen.

**Für Kliniken**
- Behandlungsplan vollständig und aktuell halten: Nur was dort steht, deckt die Anordnung (BGE 143 III 337 E. 2.4.2). Bei Medikationswechsel den Plan anpassen.
- Die Anordnung befristen und das Ziel nennen; Fixierungen und Isolationen gesondert dokumentieren (Art. 438 ZGB).
- Urteilsunfähigkeit **bezogen auf die Behandlungsbedürftigkeit** begründen, nicht bloss die Diagnose nennen.

**Für Gerichte**
- Gutachten einer unabhängigen Fachperson einholen (Art. 450e Abs. 3 ZGB) und die Folgen eines Absetzens, Alternativen und Nebenwirkungen konkret feststellen; sonst ist die Interessenabwägung nicht überprüfbar (BGE 130 I 16 E. 5.4).

---

## Leitentscheide {#leitentscheide}

| Entscheid | Gegenstand | Bedeutung |
|---|---|---|
| [BGE 125 III 169](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_005_BGE-125-III-169_1999-04-29.html) | Zwangsbehandlung im fürsorgerischen Freiheitsentzug (altes Recht) | Art. 397a ff. aZGB keine Grundlage für Zwangsbehandlung |
| [BGE 126 I 112](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_001_BGE-126-I-112_2000-05-23.html) | Zwangsmedikation und Isolierung | Anforderungen an die gesetzliche Grundlage; Verhältnismässigkeit in sachlicher und zeitlicher Hinsicht |
| [BGE 127 I 6](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_001_BGE-127-I-6_2001-03-22.html) | Basler Psychiatriegesetz | persönliche Freiheit, Menschenwürde, EMRK; Interessenabwägung |
| [BGE 127 IV 154](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_006_BGE-127-IV-154_2001-06-15.html) | Zwangsmedikation im Massnahmenvollzug | strafrechtliche Massnahme als Grundlage; Alternativmedikamente prüfen |
| [BGE 130 I 16](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_001_BGE-130-I-16_2004.html) | Depotmedikation, Zuger Gesundheitsgesetz | Prüfraster der umfassenden Interessenabwägung; Aufhebung |
| [BGE 130 IV 49](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_006_BGE-130-IV-49_2004.html) | Zuständigkeit im Massnahmenvollzug | Vollzugsbehörde ordnet an, im Rahmen des Strafurteils |
| [BGE 134 I 221](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_001_BGE-134-I-221_2008.html) | Einzelunterbringung statt Medikation | Art. 90 StGB; Verhältnismässigkeit im Vergleich zur Zwangsmedikation |
| [BGE 136 IV 97](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_006_BGE-136-IV-97_2010.html) | Hungerstreik (Rappaz) | Zwangsernährung urteilsfähiger Gefangener unter Voraussetzungen zulässig |
| [BGE 143 III 337](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_005_BGE-143-III-337_2017.html) | Begriff der Anordnung nach Art. 434 ZGB | Behandlungsplan bestimmt Inhalt; Gesamtanordnung; Duldungspflicht; Realakt anfechtbar |
| [BGer 5A_1021/2021](https://entscheidsuche.ch/docs/CH_BGer/CH_BGer_005_5A-1021-2021_2021-12-17.html) | Zwangsernährung bei Anorexie | keine akute Lebensgefahr nötig; Fixierung; Urteilsunfähige vs. Urteilsfähige |
| [BGer 5A_857/2024](https://entscheidsuche.ch/docs/CH_BGer/CH_BGer_005_5A-857-2024_2025-01-16.html) | Depotmedikation bei Schizophrenie | ernsthafter Gesundheitsschaden; Urteilsunfähigkeit; Subsidiarität |
| [BGer 5A_985/2020](https://entscheidsuche.ch/docs/CH_BGer/CH_BGer_005_5A-985-2020_2021-05-26.html) | Patientenverfügung | Verfügung muss in die gerichtliche Prüfung einfliessen |
| [BGer 5A_122/2026](https://entscheidsuche.ch/docs/CH_BGer/CH_BGer_005_5A-122-2026_2026-02-24.html) | aufschiebende Wirkung | Frage offen; Feststellung nur über Art. 454 ZGB |
| [BGer 6B_554/2021](https://entscheidsuche.ch/docs/CH_BGer/CH_BGer_006_6B-554-2021_2021-06-25.html) | Zwangsmedikation nach Art. 59 StGB | Rechtsweg, Grundlage, Interessenabwägung, Befristung |
