var NodeHelper = require("node_helper");
var pythonStarted = false;
module.exports = NodeHelper.create({
	start: function() {
		console.log("Started node_helper for MMM-DailyReadings.");
	},

	socketNotificationReceived: function(notification, payload) {
		console.log(this.name + " node helper received a socket notification: " + notification + " - Payload: " + payload);
		this.dailyReading(payload);
	},

	Daily_Readings: function() {
		var myPythonScript = "prettyreadings2.py";

		var pythonExecutable = "python";

		var DailyReadings = function (data) {
		  return String.fromCharCode.apply(null,data);
			};

		var spawn = require('child_process').spawn;
		var scriptExecution = spawn(pythonExecutable, [myPythonScript]);

		scriptExecution.stdout.on('data',(data)); {
			return (DailyReadings(data));
			}
		scriptExecution.stderr.on('data',(data)); {
			return (DailyReadings(data));
			}
		scriptExecution.on('exit',(code)); {
			return ("process quit with code : " + code);
			}
		/*scriptExecution.stdout.on('data',(data) => {
		  console.log(DailyReadings(data));
		});

		scriptExecution.stderr.on('data',(data) =>{
		  console.log(DailyReadings(data));
		});

		scriptExecution.on('exit',(code) => {
		  console.log("Process quit with code : " + code);
		});
		*/
		if(code === 0) {
				console.log(DailyReadings(data));
				var result = JSON.parse(DailyReadings(data));
				self.sendSocketNotification('Daily_Readings_Result',result);
		}
	}
});
