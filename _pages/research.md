---
layout: page
title: research
permalink: /research/
description:
nav: true
nav_order: 1
---

My research investigates how cryptographic and machine-learning implementations behave under realistic physical attacks. I combine experimental evaluation with automated analysis and the design of practical countermeasures, with the aim of bridging the gap between theoretical security guarantees and implementation-level security.

## Physical Security of Cryptographic Implementations

My work addresses side-channel analysis and fault injection attacks on cryptographic devices, from microcontroller software to hardware implementations. A particular focus is automating security evaluation and understanding how architectural and algorithmic choices affect resistance to physical attacks.

<div class="research-photo-grid research-photo-grid-3" role="group" aria-label="Cryptographic implementation security experiments">
  <figure>
    <a href="{{ '/assets/img/research-pulse-generator.webp' | relative_url }}"><img src="{{ '/assets/img/research-pulse-generator.webp' | relative_url }}" alt="AVIR pulse generator and Arduino UNO board" loading="lazy" decoding="async"></a>
    <figcaption>Pulse generator and microcontroller test platform.</figcaption>
  </figure>
  <figure>
    <a href="{{ '/assets/img/research-virtex5-ir.webp' | relative_url }}"><img src="{{ '/assets/img/research-virtex5-ir.webp' | relative_url }}" alt="Infrared microscopy image of a Virtex-5 FPGA" loading="lazy" decoding="async"></a>
    <figcaption>Infrared microscopy of a Virtex-5 FPGA.</figcaption>
  </figure>
  <figure>
    <a href="{{ '/assets/img/research-side-channel.webp' | relative_url }}"><img src="{{ '/assets/img/research-side-channel.webp' | relative_url }}" alt="Oscilloscope, laptop and ChipWhisperer measurement setup" loading="lazy" decoding="async"></a>
    <figcaption>Oscilloscope and ChipWhisperer side-channel measurement setup.</figcaption>
  </figure>
</div>

**Research topics**

- Laser and electromagnetic fault injection, fault characterization, and differential fault analysis.
- Automated analysis of software implementations and fault-resistant encodings.
- Side-channel leakage, combined physical attacks, and implementation countermeasures.
- Cryptographic primitives designed with implementation security in mind.

**Representative publications**

- [Fully Automated Differential Fault Analysis on Software Implementations of Block Ciphers]({{ '/publications/' | relative_url }}#DBLP:journals/tches/HouBZL19) — TCHES 2019.
- [Fault Attacks Made Easy: Differential Fault Analysis Automation on Assembly Code]({{ '/publications/' | relative_url }}#DBLP:journals/tches/BreierHL18) — TCHES 2018.
- [DEFAULT: Cipher-Level Resistance Against Differential Fault Attack]({{ '/publications/' | relative_url }}#baksi2021default) — ASIACRYPT 2021.
- [A Survey on Fault Attacks on Symmetric Key Cryptosystems]({{ '/publications/' | relative_url }}#baksi2022survey) — ACM Computing Surveys 2023.

---

## Hardware Security of Edge AI

This research direction investigates the implementation-level security of neural networks deployed on embedded and edge devices. My work explores how physical attacks can affect model confidentiality and integrity, how leakage and fault susceptibility can be measured, and how countermeasures can be designed for resource-constrained platforms.

<div class="research-photo-grid research-photo-grid-2" role="group" aria-label="Embedded and Edge AI security experiments">
  <figure>
    <a href="{{ '/assets/img/research-embedded-emfi.webp' | relative_url }}"><img src="{{ '/assets/img/research-embedded-emfi.webp' | relative_url }}" alt="ChipSHOUTER probe above an embedded development board" loading="lazy" decoding="async"></a>
    <figcaption>Electromagnetic fault injection on an embedded development board.</figcaption>
  </figure>
  <figure>
    <a href="{{ '/assets/img/research-ncs2-emfi.webp' | relative_url }}"><img src="{{ '/assets/img/research-ncs2-emfi.webp' | relative_url }}" alt="ChipSHOUTER and decased Intel Neural Compute Stick 2 on a positioning platform" loading="lazy" decoding="async"></a>
    <figcaption>EMFI evaluation setup for an Intel Neural Compute Stick 2.</figcaption>
  </figure>
</div>

**Research topics**

- Fault attacks on neural-network inference and training.
- Model extraction, weight recovery, and side-channel leakage assessment.
- Fault characterization of embedded neural-network accelerators.
- Secure and fault-resilient neural-network implementations, including encoding and shuffling countermeasures.

**Representative publications**

- [Practical Fault Attack on Deep Neural Networks]({{ '/publications/' | relative_url }}#breier2018practical) — ACM CCS 2018.
- [FooBaR: Fault Fooling Backdoor Attack on Neural Network Training]({{ '/publications/' | relative_url }}#breier2022foobar) — IEEE TDSC 2023.
- [Make Shuffling Great Again: A Side-Channel Resistant Fisher-Yates Algorithm for Protecting Neural Networks]({{ '/publications/' | relative_url }}#tvlsi2025) — IEEE TVLSI 2025.
- [DeepNcode: Encoding-Based Protection against Bit-Flip Attacks on Neural Networks]({{ '/publications/' | relative_url }}#velvcicky2024deepncode) — IEEE TETC, accepted, 2026.
- [Guess My Weight: Profiled Side-Channel Recovery of Floating-Point Neural-Network Weights]({{ '/publications/' | relative_url }}#fillo2026guess) — SPACE 2026, accepted.

For recent manuscripts, see the [preprints section]({{ '/publications/' | relative_url }}#preprints).

<style>
.research-photo-grid { display: grid; gap: 1rem; margin: 1.5rem 0; }
.research-photo-grid-3 { grid-template-columns: repeat(3, minmax(0, 1fr)); }
.research-photo-grid-2 { grid-template-columns: repeat(2, minmax(0, 1fr)); max-width: 680px; margin-left: auto; margin-right: auto; }
.research-photo-grid figure { margin: 0; min-width: 0; }
.research-photo-grid a { display: block; border-radius: 6px; background: rgba(128,128,128,.07); overflow: hidden; }
.research-photo-grid img { display: block; width: 100%; height: 180px; object-fit: contain; }
.research-photo-grid-2 img { height: 300px; }
.research-photo-grid figcaption { font-size: .85rem; line-height: 1.4; margin: .55rem 0 0; text-align: center; color: var(--global-text-color-light, inherit); }
@media (max-width: 575px) { .research-photo-grid-3 { grid-template-columns: repeat(2, minmax(0, 1fr)); } .research-photo-grid img { height: 145px; } .research-photo-grid-2 img { height: 220px; } }
</style>
