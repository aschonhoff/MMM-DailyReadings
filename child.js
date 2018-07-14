var myPythonScript = "prettyreadings2.py";

var pythonExecutable = "python";

var DailyReadings = function (data) {
  return String.fromCharCode.apply(null,data);
};

var spawn = require('child_process').spawn;
var scriptExecution = spawn(pythonExecutable, [myPythonScript]);

scriptExecution.stdout.on('data',(data) => {
  console.log(DailyReadings(data));
});

scriptExecution.stderr.on('data',(data) =>{
  console.log(DailyReadings(data));
});

scriptExecution.on('exit',(code) => {
  console.log("Process quit with code : " + code);
});
