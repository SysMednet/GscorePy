var CanvasApp = function () {
			var cy;
			var cyto_scene;

			return {
				one: function () {
					if (cyto_scene) {
						cyto_scene = document.getElementById('cyto_scene');
						cyto_scene.removeChild(cyto_scene.firstElementChild);
						var elem = document.createElement("div");
						elem.id = 'cy';
						cyto_scene.appendChild(elem);
					}else{
						cyto_scene = document.getElementById('cyto_scene');
						var elem = document.createElement("div");
						elem.id = 'cy';
						cyto_scene.appendChild(elem);
					}

					cy = $(elem).cytoscape({
							pan: {
								x: 600,
								y: 400
								},
							boxSelectionEnabled: false,
							autounselectify: false,
							panningEnabled: true,
							zoom: 1,
							minZoom: 0.25,
							maxZoom: 2.5,
							wheelSensitivity: 0.4,
							elements: [
									{"group":"nodes", "data": { "id": "DEG list","shape": "diamond","color":"#ACD6FF"} },
									{"group":"nodes", "data": { "id": "Influenza A","shape": "roundrectangle","color":"#FF9797"}},
									{"group":"edges", "data": { "id": "e0", "source": "DEG list", "target": "Influenza A","width": "13.00" }},
									{"group":"nodes", "data": { "id": "Measles","shape": "roundrectangle","color":"#FF9797"}},
									{"group":"edges", "data": { "id": "e1", "source": "DEG list", "target": "Measles","width": "11.90" }},
									{"group":"nodes", "data": { "id": "Coronavirus disease - COVID-19","shape": "roundrectangle","color":"#FF9797"}},
									{"group":"edges", "data": { "id": "e2", "source": "DEG list", "target": "Coronavirus disease - COVID-19","width": "9.26" }},
									{"group":"nodes", "data": { "id": "Cell cycle","shape": "roundrectangle","color":"#FF9797"}},
									{"group":"edges", "data": { "id": "e3", "source": "DEG list", "target": "Cell cycle","width": "8.11" }},
									{"group":"nodes", "data": { "id": "Herpes simplex virus 1 infection","shape": "roundrectangle","color":"#FF9797"}},
									{"group":"edges", "data": { "id": "e4", "source": "DEG list", "target": "Herpes simplex virus 1 infection","width": "7.30" }},
									{"group":"nodes", "data": { "id": "Oocyte meiosis","shape": "roundrectangle","color":"#FF9797"}},
									{"group":"edges", "data": { "id": "e5", "source": "DEG list", "target": "Oocyte meiosis","width": "6.02" }},
									{"group":"nodes", "data": { "id": "Hepatitis C","shape": "roundrectangle","color":"#FF9797"}},
									{"group":"edges", "data": { "id": "e6", "source": "DEG list", "target": "Hepatitis C","width": "5.78" }},
									{"group":"nodes", "data": { "id": "Necroptosis","shape": "roundrectangle","color":"#FF9797"}},
									{"group":"edges", "data": { "id": "e7", "source": "DEG list", "target": "Necroptosis","width": "3.68" }},
									{"group":"nodes", "data": { "id": "DNA replication","shape": "roundrectangle","color":"#FF9797"}},
									{"group":"edges", "data": { "id": "e8", "source": "DEG list", "target": "DNA replication","width": "3.46" }},
									{"group":"nodes", "data": { "id": "p53 signaling pathway","shape": "roundrectangle","color":"#FF9797"}},
									{"group":"edges", "data": { "id": "e9", "source": "DEG list", "target": "p53 signaling pathway","width": "3.00" }}]
						,
						style: [{
							selector: 'node',
							style: {
								'background-color': 'data(color)',
								'label': 'data(id)',
								'shape': 'data(shape)',
								'width': 50,
								'height': 50,
								"text-wrap": "wrap",
								"text-max-width": 70,
								"text-valign": "center",
								"font-size": "12px"
							}
						},
						{
							selector: 'edge',
							style: {
								'width': 'data(width)',
								'line-color': '#ccc',
								'target-arrow-color': '#ccc'
							}
						}
						],
						layout: {
							name: 'concentric',
							fit: true,
							minNodeSpacing: 20,
							concentric: function(node) {
								return node.degree();
							},
							levelWidth: function(nodes) {
								return 2;
							}
						}
					}).cytoscape('get');
					cy.panzoom({});
				},
				two: function () {
					if (cyto_scene) {
						cyto_scene = document.getElementById('cyto_scene');
						cyto_scene.removeChild(cyto_scene.firstElementChild);
						var elem = document.createElement("div");
						elem.id = 'cy';
						cyto_scene.appendChild(elem);
					}else{
						cyto_scene = document.getElementById('cyto_scene');
						var elem = document.createElement("div");
						elem.id = 'cy';
						cyto_scene.appendChild(elem);
					}

					cy = $(elem).cytoscape({
							pan: {
								x: 600,
								y: 400
								},
							boxSelectionEnabled: false,
							autounselectify: false,
							panningEnabled: true,
							zoom: 1,
							minZoom: 0.25,
							maxZoom: 2.5,
							wheelSensitivity: 0.4,
							elements: [
									{"group":"nodes", "data": { "id": "DEG list","shape": "diamond","color":"#ACD6FF"} },
									{"group":"nodes", "data": { "id": "Influenza A","shape": "roundrectangle","color":"#FF9797"}},
									{"group":"edges", "data": { "id": "e0", "source": "DEG list", "target": "Influenza A","width": "13.00" }},
									{"group":"nodes", "data": { "id": "Measles","shape": "roundrectangle","color":"#FF9797"}},
									{"group":"edges", "data": { "id": "e1", "source": "DEG list", "target": "Measles","width": "12.19" }},
									{"group":"nodes", "data": { "id": "Coronavirus disease - COVID-19","shape": "roundrectangle","color":"#FF9797"}},
									{"group":"edges", "data": { "id": "e2", "source": "DEG list", "target": "Coronavirus disease - COVID-19","width": "10.25" }},
									{"group":"nodes", "data": { "id": "Cell cycle","shape": "roundrectangle","color":"#FF9797"}},
									{"group":"edges", "data": { "id": "e3", "source": "DEG list", "target": "Cell cycle","width": "9.41" }},
									{"group":"nodes", "data": { "id": "Herpes simplex virus 1 infection","shape": "roundrectangle","color":"#FF9797"}},
									{"group":"edges", "data": { "id": "e4", "source": "DEG list", "target": "Herpes simplex virus 1 infection","width": "8.82" }},
									{"group":"nodes", "data": { "id": "Oocyte meiosis","shape": "roundrectangle","color":"#FF9797"}},
									{"group":"edges", "data": { "id": "e5", "source": "DEG list", "target": "Oocyte meiosis","width": "7.87" }},
									{"group":"nodes", "data": { "id": "Hepatitis C","shape": "roundrectangle","color":"#FF9797"}},
									{"group":"edges", "data": { "id": "e6", "source": "DEG list", "target": "Hepatitis C","width": "7.69" }},
									{"group":"nodes", "data": { "id": "Necroptosis","shape": "roundrectangle","color":"#FF9797"}},
									{"group":"edges", "data": { "id": "e7", "source": "DEG list", "target": "Necroptosis","width": "6.15" }},
									{"group":"nodes", "data": { "id": "DNA replication","shape": "roundrectangle","color":"#FF9797"}},
									{"group":"edges", "data": { "id": "e8", "source": "DEG list", "target": "DNA replication","width": "5.99" }},
									{"group":"nodes", "data": { "id": "p53 signaling pathway","shape": "roundrectangle","color":"#FF9797"}},
									{"group":"edges", "data": { "id": "e9", "source": "DEG list", "target": "p53 signaling pathway","width": "5.65" }},
									{"group":"nodes", "data": { "id": "Progesterone-mediated oocyte maturation","shape": "roundrectangle","color":"#FF9797"}},
									{"group":"edges", "data": { "id": "e10", "source": "DEG list", "target": "Progesterone-mediated oocyte maturation","width": "4.60" }},
									{"group":"nodes", "data": { "id": "NOD-like receptor signaling pathway","shape": "roundrectangle","color":"#FF9797"}},
									{"group":"edges", "data": { "id": "e11", "source": "DEG list", "target": "NOD-like receptor signaling pathway","width": "4.34" }},
									{"group":"nodes", "data": { "id": "RNA degradation","shape": "roundrectangle","color":"#FF9797"}},
									{"group":"edges", "data": { "id": "e12", "source": "DEG list", "target": "RNA degradation","width": "4.02" }},
									{"group":"nodes", "data": { "id": "Pyrimidine metabolism","shape": "roundrectangle","color":"#FF9797"}},
									{"group":"edges", "data": { "id": "e13", "source": "DEG list", "target": "Pyrimidine metabolism","width": "3.99" }},
									{"group":"nodes", "data": { "id": "Nucleotide metabolism","shape": "roundrectangle","color":"#FF9797"}},
									{"group":"edges", "data": { "id": "e14", "source": "DEG list", "target": "Nucleotide metabolism","width": "3.99" }},
									{"group":"nodes", "data": { "id": "RIG-I-like receptor signaling pathway","shape": "roundrectangle","color":"#FF9797"}},
									{"group":"edges", "data": { "id": "e15", "source": "DEG list", "target": "RIG-I-like receptor signaling pathway","width": "3.95" }},
									{"group":"nodes", "data": { "id": "Chemokine signaling pathway","shape": "roundrectangle","color":"#FF9797"}},
									{"group":"edges", "data": { "id": "e16", "source": "DEG list", "target": "Chemokine signaling pathway","width": "3.78" }},
									{"group":"nodes", "data": { "id": "C-type lectin receptor signaling pathway","shape": "roundrectangle","color":"#FF9797"}},
									{"group":"edges", "data": { "id": "e17", "source": "DEG list", "target": "C-type lectin receptor signaling pathway","width": "3.78" }},
									{"group":"nodes", "data": { "id": "Epstein-Barr virus infection","shape": "roundrectangle","color":"#FF9797"}},
									{"group":"edges", "data": { "id": "e18", "source": "DEG list", "target": "Epstein-Barr virus infection","width": "3.75" }},
									{"group":"nodes", "data": { "id": "Cytosolic DNA-sensing pathway","shape": "roundrectangle","color":"#FF9797"}},
									{"group":"edges", "data": { "id": "e19", "source": "DEG list", "target": "Cytosolic DNA-sensing pathway","width": "3.71" }},
									{"group":"nodes", "data": { "id": "Protein processing in endoplasmic reticulum","shape": "roundrectangle","color":"#FF9797"}},
									{"group":"edges", "data": { "id": "e20", "source": "DEG list", "target": "Protein processing in endoplasmic reticulum","width": "3.60" }},
									{"group":"nodes", "data": { "id": "Glutathione metabolism","shape": "roundrectangle","color":"#FF9797"}},
									{"group":"edges", "data": { "id": "e21", "source": "DEG list", "target": "Glutathione metabolism","width": "3.54" }},
									{"group":"nodes", "data": { "id": "Purine metabolism","shape": "roundrectangle","color":"#FF9797"}},
									{"group":"edges", "data": { "id": "e22", "source": "DEG list", "target": "Purine metabolism","width": "3.31" }},
									{"group":"nodes", "data": { "id": "Base excision repair","shape": "roundrectangle","color":"#FF9797"}},
									{"group":"edges", "data": { "id": "e23", "source": "DEG list", "target": "Base excision repair","width": "3.00" }},
									{"group":"nodes", "data": { "id": "Hepatitis B","shape": "roundrectangle","color":"#FF9797"}},
									{"group":"edges", "data": { "id": "e24", "source": "DEG list", "target": "Hepatitis B","width": "3.00" }}]
						,
						style: [{
							selector: 'node',
							style: {
								'background-color': 'data(color)',
								'label': 'data(id)',
								'shape': 'data(shape)',
								'width': 50,
								'height': 50,
								"text-wrap": "wrap",
								"text-max-width": 70,
								"text-valign": "center",
								"font-size": "12px"
							}
						},
						{
							selector: 'edge',
							style: {
								'width': 'data(width)',
								'line-color': '#ccc',
								'target-arrow-color': '#ccc'
							}
						}
						],
						layout: {
							name: 'concentric',
							fit: true,
							minNodeSpacing: 20,
							concentric: function(node) {
								return node.degree();
							},
							levelWidth: function(nodes) {
								return 2;
							}
						}
					}).cytoscape('get');
					cy.panzoom({});
				},
				three: function () {
					if (cyto_scene) {
						cyto_scene = document.getElementById('cyto_scene');
						cyto_scene.removeChild(cyto_scene.firstElementChild);
						var elem = document.createElement("div");
						elem.id = 'cy';
						cyto_scene.appendChild(elem);
					}else{
						cyto_scene = document.getElementById('cyto_scene');
						var elem = document.createElement("div");
						elem.id = 'cy';
						cyto_scene.appendChild(elem);
					}

					cy = $(elem).cytoscape({
							pan: {
								x: 600,
								y: 400
								},
							boxSelectionEnabled: false,
							autounselectify: false,
							panningEnabled: true,
							zoom: 1,
							minZoom: 0.25,
							maxZoom: 2.5,
							wheelSensitivity: 0.4,
							elements: [
									{"group":"nodes", "data": { "id": "DEG list","shape": "diamond","color":"#ACD6FF"} },
									{"group":"nodes", "data": { "id": "Influenza A","shape": "roundrectangle","color":"#FF9797"}},
									{"group":"edges", "data": { "id": "e0", "source": "DEG list", "target": "Influenza A","width": "13.00" }},
									{"group":"nodes", "data": { "id": "Measles","shape": "roundrectangle","color":"#FF9797"}},
									{"group":"edges", "data": { "id": "e1", "source": "DEG list", "target": "Measles","width": "12.28" }},
									{"group":"nodes", "data": { "id": "Coronavirus disease - COVID-19","shape": "roundrectangle","color":"#FF9797"}},
									{"group":"edges", "data": { "id": "e2", "source": "DEG list", "target": "Coronavirus disease - COVID-19","width": "10.57" }},
									{"group":"nodes", "data": { "id": "Cell cycle","shape": "roundrectangle","color":"#FF9797"}},
									{"group":"edges", "data": { "id": "e3", "source": "DEG list", "target": "Cell cycle","width": "9.82" }},
									{"group":"nodes", "data": { "id": "Herpes simplex virus 1 infection","shape": "roundrectangle","color":"#FF9797"}},
									{"group":"edges", "data": { "id": "e4", "source": "DEG list", "target": "Herpes simplex virus 1 infection","width": "9.30" }},
									{"group":"nodes", "data": { "id": "Oocyte meiosis","shape": "roundrectangle","color":"#FF9797"}},
									{"group":"edges", "data": { "id": "e5", "source": "DEG list", "target": "Oocyte meiosis","width": "8.47" }},
									{"group":"nodes", "data": { "id": "Hepatitis C","shape": "roundrectangle","color":"#FF9797"}},
									{"group":"edges", "data": { "id": "e6", "source": "DEG list", "target": "Hepatitis C","width": "8.31" }},
									{"group":"nodes", "data": { "id": "Necroptosis","shape": "roundrectangle","color":"#FF9797"}},
									{"group":"edges", "data": { "id": "e7", "source": "DEG list", "target": "Necroptosis","width": "6.95" }},
									{"group":"nodes", "data": { "id": "DNA replication","shape": "roundrectangle","color":"#FF9797"}},
									{"group":"edges", "data": { "id": "e8", "source": "DEG list", "target": "DNA replication","width": "6.80" }},
									{"group":"nodes", "data": { "id": "p53 signaling pathway","shape": "roundrectangle","color":"#FF9797"}},
									{"group":"edges", "data": { "id": "e9", "source": "DEG list", "target": "p53 signaling pathway","width": "6.50" }},
									{"group":"nodes", "data": { "id": "Progesterone-mediated oocyte maturation","shape": "roundrectangle","color":"#FF9797"}},
									{"group":"edges", "data": { "id": "e10", "source": "DEG list", "target": "Progesterone-mediated oocyte maturation","width": "5.58" }},
									{"group":"nodes", "data": { "id": "NOD-like receptor signaling pathway","shape": "roundrectangle","color":"#FF9797"}},
									{"group":"edges", "data": { "id": "e11", "source": "DEG list", "target": "NOD-like receptor signaling pathway","width": "5.35" }},
									{"group":"nodes", "data": { "id": "RNA degradation","shape": "roundrectangle","color":"#FF9797"}},
									{"group":"edges", "data": { "id": "e12", "source": "DEG list", "target": "RNA degradation","width": "5.06" }},
									{"group":"nodes", "data": { "id": "Pyrimidine metabolism","shape": "roundrectangle","color":"#FF9797"}},
									{"group":"edges", "data": { "id": "e13", "source": "DEG list", "target": "Pyrimidine metabolism","width": "5.03" }},
									{"group":"nodes", "data": { "id": "Nucleotide metabolism","shape": "roundrectangle","color":"#FF9797"}},
									{"group":"edges", "data": { "id": "e14", "source": "DEG list", "target": "Nucleotide metabolism","width": "5.03" }},
									{"group":"nodes", "data": { "id": "RIG-I-like receptor signaling pathway","shape": "roundrectangle","color":"#FF9797"}},
									{"group":"edges", "data": { "id": "e15", "source": "DEG list", "target": "RIG-I-like receptor signaling pathway","width": "5.00" }},
									{"group":"nodes", "data": { "id": "Chemokine signaling pathway","shape": "roundrectangle","color":"#FF9797"}},
									{"group":"edges", "data": { "id": "e16", "source": "DEG list", "target": "Chemokine signaling pathway","width": "4.85" }},
									{"group":"nodes", "data": { "id": "C-type lectin receptor signaling pathway","shape": "roundrectangle","color":"#FF9797"}},
									{"group":"edges", "data": { "id": "e17", "source": "DEG list", "target": "C-type lectin receptor signaling pathway","width": "4.85" }},
									{"group":"nodes", "data": { "id": "Epstein-Barr virus infection","shape": "roundrectangle","color":"#FF9797"}},
									{"group":"edges", "data": { "id": "e18", "source": "DEG list", "target": "Epstein-Barr virus infection","width": "4.82" }},
									{"group":"nodes", "data": { "id": "Cytosolic DNA-sensing pathway","shape": "roundrectangle","color":"#FF9797"}},
									{"group":"edges", "data": { "id": "e19", "source": "DEG list", "target": "Cytosolic DNA-sensing pathway","width": "4.78" }},
									{"group":"nodes", "data": { "id": "Protein processing in endoplasmic reticulum","shape": "roundrectangle","color":"#FF9797"}},
									{"group":"edges", "data": { "id": "e20", "source": "DEG list", "target": "Protein processing in endoplasmic reticulum","width": "4.69" }},
									{"group":"nodes", "data": { "id": "Glutathione metabolism","shape": "roundrectangle","color":"#FF9797"}},
									{"group":"edges", "data": { "id": "e21", "source": "DEG list", "target": "Glutathione metabolism","width": "4.64" }},
									{"group":"nodes", "data": { "id": "Purine metabolism","shape": "roundrectangle","color":"#FF9797"}},
									{"group":"edges", "data": { "id": "e22", "source": "DEG list", "target": "Purine metabolism","width": "4.43" }},
									{"group":"nodes", "data": { "id": "Base excision repair","shape": "roundrectangle","color":"#FF9797"}},
									{"group":"edges", "data": { "id": "e23", "source": "DEG list", "target": "Base excision repair","width": "4.16" }},
									{"group":"nodes", "data": { "id": "Hepatitis B","shape": "roundrectangle","color":"#FF9797"}},
									{"group":"edges", "data": { "id": "e24", "source": "DEG list", "target": "Hepatitis B","width": "4.16" }},
									{"group":"nodes", "data": { "id": "Non-homologous end-joining","shape": "roundrectangle","color":"#FF9797"}},
									{"group":"edges", "data": { "id": "e25", "source": "DEG list", "target": "Non-homologous end-joining","width": "4.16" }},
									{"group":"nodes", "data": { "id": "Growth hormone synthesis, secretion and action","shape": "roundrectangle","color":"#FF9797"}},
									{"group":"edges", "data": { "id": "e26", "source": "DEG list", "target": "Growth hormone synthesis, secretion and action","width": "3.84" }},
									{"group":"nodes", "data": { "id": "AGE-RAGE signaling pathway in diabetic complications","shape": "roundrectangle","color":"#FF9797"}},
									{"group":"edges", "data": { "id": "e27", "source": "DEG list", "target": "AGE-RAGE signaling pathway in diabetic complications","width": "3.84" }},
									{"group":"nodes", "data": { "id": "Prolactin signaling pathway","shape": "roundrectangle","color":"#FF9797"}},
									{"group":"edges", "data": { "id": "e28", "source": "DEG list", "target": "Prolactin signaling pathway","width": "3.84" }},
									{"group":"nodes", "data": { "id": "Toxoplasmosis","shape": "roundrectangle","color":"#FF9797"}},
									{"group":"edges", "data": { "id": "e29", "source": "DEG list", "target": "Toxoplasmosis","width": "3.84" }},
									{"group":"nodes", "data": { "id": "Th1 and Th2 cell differentiation","shape": "roundrectangle","color":"#FF9797"}},
									{"group":"edges", "data": { "id": "e30", "source": "DEG list", "target": "Th1 and Th2 cell differentiation","width": "3.84" }},
									{"group":"nodes", "data": { "id": "Toll-like receptor signaling pathway","shape": "roundrectangle","color":"#FF9797"}},
									{"group":"edges", "data": { "id": "e31", "source": "DEG list", "target": "Toll-like receptor signaling pathway","width": "3.84" }},
									{"group":"nodes", "data": { "id": "NF-kappa B signaling pathway","shape": "roundrectangle","color":"#FF9797"}},
									{"group":"edges", "data": { "id": "e32", "source": "DEG list", "target": "NF-kappa B signaling pathway","width": "3.84" }},
									{"group":"nodes", "data": { "id": "Notch signaling pathway","shape": "roundrectangle","color":"#FF9797"}},
									{"group":"edges", "data": { "id": "e33", "source": "DEG list", "target": "Notch signaling pathway","width": "3.73" }},
									{"group":"nodes", "data": { "id": "Kaposi sarcoma-associated herpesvirus infection","shape": "roundrectangle","color":"#FF9797"}},
									{"group":"edges", "data": { "id": "e34", "source": "DEG list", "target": "Kaposi sarcoma-associated herpesvirus infection","width": "3.70" }},
									{"group":"nodes", "data": { "id": "Th17 cell differentiation","shape": "roundrectangle","color":"#FF9797"}},
									{"group":"edges", "data": { "id": "e35", "source": "DEG list", "target": "Th17 cell differentiation","width": "3.68" }},
									{"group":"nodes", "data": { "id": "Cellular senescence","shape": "roundrectangle","color":"#FF9797"}},
									{"group":"edges", "data": { "id": "e36", "source": "DEG list", "target": "Cellular senescence","width": "3.57" }},
									{"group":"nodes", "data": { "id": "Signaling pathways regulating pluripotency of stem cells","shape": "roundrectangle","color":"#FF9797"}},
									{"group":"edges", "data": { "id": "e37", "source": "DEG list", "target": "Signaling pathways regulating pluripotency of stem cells","width": "3.39" }},
									{"group":"nodes", "data": { "id": "JAK-STAT signaling pathway","shape": "roundrectangle","color":"#FF9797"}},
									{"group":"edges", "data": { "id": "e38", "source": "DEG list", "target": "JAK-STAT signaling pathway","width": "3.34" }},
									{"group":"nodes", "data": { "id": "Platinum drug resistance","shape": "roundrectangle","color":"#FF9797"}},
									{"group":"edges", "data": { "id": "e39", "source": "DEG list", "target": "Platinum drug resistance","width": "3.32" }},
									{"group":"nodes", "data": { "id": "Fanconi anemia pathway","shape": "roundrectangle","color":"#FF9797"}},
									{"group":"edges", "data": { "id": "e40", "source": "DEG list", "target": "Fanconi anemia pathway","width": "3.21" }},
									{"group":"nodes", "data": { "id": "Protein export","shape": "roundrectangle","color":"#FF9797"}},
									{"group":"edges", "data": { "id": "e41", "source": "DEG list", "target": "Protein export","width": "3.09" }},
									{"group":"nodes", "data": { "id": "Drug metabolism - other enzymes","shape": "roundrectangle","color":"#FF9797"}},
									{"group":"edges", "data": { "id": "e42", "source": "DEG list", "target": "Drug metabolism - other enzymes","width": "3.08" }},
									{"group":"nodes", "data": { "id": "ABC transporters","shape": "roundrectangle","color":"#FF9797"}},
									{"group":"edges", "data": { "id": "e43", "source": "DEG list", "target": "ABC transporters","width": "3.04" }},
									{"group":"nodes", "data": { "id": "Fat digestion and absorption","shape": "roundrectangle","color":"#FF9797"}},
									{"group":"edges", "data": { "id": "e44", "source": "DEG list", "target": "Fat digestion and absorption","width": "3.04" }},
									{"group":"nodes", "data": { "id": "Ubiquitin mediated proteolysis","shape": "roundrectangle","color":"#FF9797"}},
									{"group":"edges", "data": { "id": "e45", "source": "DEG list", "target": "Ubiquitin mediated proteolysis","width": "3.02" }},
									{"group":"nodes", "data": { "id": "Glycolysis / Gluconeogenesis","shape": "roundrectangle","color":"#FF9797"}},
									{"group":"edges", "data": { "id": "e46", "source": "DEG list", "target": "Glycolysis / Gluconeogenesis","width": "3.00" }},
									{"group":"nodes", "data": { "id": "Pertussis","shape": "roundrectangle","color":"#FF9797"}},
									{"group":"edges", "data": { "id": "e47", "source": "DEG list", "target": "Pertussis","width": "3.00" }},
									{"group":"nodes", "data": { "id": "Hippo signaling pathway","shape": "roundrectangle","color":"#FF9797"}},
									{"group":"edges", "data": { "id": "e48", "source": "DEG list", "target": "Hippo signaling pathway","width": "3.00" }},
									{"group":"nodes", "data": { "id": "Galactose metabolism","shape": "roundrectangle","color":"#FF9797"}},
									{"group":"edges", "data": { "id": "e49", "source": "DEG list", "target": "Galactose metabolism","width": "3.00" }}]
						,
						style: [{
							selector: 'node',
							style: {
								'background-color': 'data(color)',
								'label': 'data(id)',
								'shape': 'data(shape)',
								'width': 50,
								'height': 50,
								"text-wrap": "wrap",
								"text-max-width": 70,
								"text-valign": "center",
								"font-size": "12px"
							}
						},
						{
							selector: 'edge',
							style: {
								'width': 'data(width)',
								'line-color': '#ccc',
								'target-arrow-color': '#ccc'
							}
						}
						],
						layout: {
							name: 'concentric',
							fit: true,
							minNodeSpacing: 20,
							concentric: function(node) {
								return node.degree();
							},
							levelWidth: function(nodes) {
								return 2;
							}
						}
					}).cytoscape('get');
					cy.panzoom({});
				}
			}
		};
		var network = new CanvasApp();