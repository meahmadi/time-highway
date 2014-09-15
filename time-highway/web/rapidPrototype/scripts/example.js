$(function(){ // on dom ready

$('#cy').cytoscape({
  hideEdgesOnViewport: true,
  hideLabelsOnViewport: true,
  textureOnViewport : true,
  panningEnabled: true,
  userPanningEnabled: true,
  style: [
    {
      selector: 'node',
      css: {
        'content': 'data(name)',
		'font-family': 'MJ_Sayeh-1',
        'font-size': 14,
        'text-valign': 'center',
        'text-halign': 'center',
		'min-zoomed-font-size': 5,
		'background-color': '#aaaabb',
      }
    },
	{
		selector: '$node > node',
		css: {
			'text-valign': 'top',
			'background-color': '#aaaaff',
			'shape':'roundrectangle',
		}
	},
    {
      selector: 'edge',
      css: {
        'target-arrow-shape': 'triangle',
		/*'curve-style':'haystack',*/
      }
    },
    {
      selector: ':selected',
      css: {
        'background-color': 'yellow',
        'line-color': 'black',
        'target-arrow-color': 'black',
        'source-arrow-color': 'black'
      }
    }
  ],
  
  elements: {
    nodes: [
    ],
    edges: [
    ]
  },
  
  layout: {
    name: 'cose',
	ready               : function() {},
    // Called on `layoutstop`
    stop                : function() {},
    // Number of iterations between consecutive screen positions update (0 -> only updated on the end)
    refresh             : 0,
    // Whether to fit the network view after when done
    fit                 : true, 
    // Padding on fit
    padding             : 100, 
    // Whether to randomize node positions on the beginning
    randomize           : true,
    // Whether to use the JS console to print debug messages
    debug               : false,
    // Node repulsion (non overlapping) multiplier
    nodeRepulsion       : 10000,
    // Node repulsion (overlapping) multiplier
    nodeOverlap         : 10,
    // Ideal edge (non nested) length
    idealEdgeLength     : 10,
    // Divisor to compute edge forces
    edgeElasticity      : 100,
    // Nesting factor (multiplier) to compute ideal edge length for nested edges
    nestingFactor       : 5, 
    // Gravity force (constant)
    gravity             : 250, 
    // Maximum number of iterations to perform
    numIter             : 100,
    // Initial temperature (maximum node displacement)
    initialTemp         : 200,
    // Cooling factor (how the temperature is reduced between consecutive iterations
    coolingFactor       : 0.95, 
    // Lower temperature threshold (below this point the layout will end)
    minTemp             : 1	
  },
  
  ready: function(){
    window.cy = this;
	
	var grp1cnt = 7;
	var grp2cnt = 3;
	var grp3cnt = 7;
	
	var lastp = "1";
	var lastc = "1";
	var lastk = "1";
	var nodes = []
	for(var i=0;i<grp1cnt;i++){
		var pid = 'p'+i;
		nodes.push({group:"nodes",
					data:{id:pid, name: 'داستان '+i,},	});
		nodes.push({ group:"edges", data: { id: 'l'+pid, source: lastp, target: pid }, });
		for(var j=0;j<grp2cnt;j++){
			var cid = 'c'+i+'-'+j;
			nodes.push({group:"nodes",
					data:{ id:cid, name: 'زیر داستان '+j, parent: pid,},});
			nodes.push({ group:"edges", data: { id: 'l'+cid, source: lastc, target: cid }, });
			for(var k=0; k<grp3cnt;k++){
				var kid = 'k'+i+'-'+j+"-"+k;
				nodes.push({group:"nodes",
						data:{ id:kid, name: 'واقعه '+k, parent: cid,},
						position:{x:1000+(j*grp3cnt+k)*60,y:80*i},});
				nodes.push({ group:"edges", data: { id: 'l'+kid, source: lastk, target: kid }, });
				lastk = kid;
			}
			lastc = cid;
		}
		lastp = pid
	}
	//console.log(nodes);
	cy.add(nodes);
	
	cy.elements().qtip({
		content: {
			text: function(){ return 'شما کلیک کرده‌اید بر روی ' + this.id() },
			button: true,
		},
		position: {
			my: 'top center',
			at: 'bottom center'
		},
	});	
	
  }
});
});