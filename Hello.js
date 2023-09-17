const { ethers } = require('hardhat');
const fs = require('fs');
const csv = require('csv-parser');

async function main() {
  // Load the contract
  const StudentDataset = await ethers.getContractFactory('StudentDataset');

  // Initialize arrays to store CSV data
  const courseNames = [];
  const dates = [];
  const certificateUrls = [];
  const instructorNames = [];
  const studentNames = [];
  const courseLengths = [];

  // Read data from CSV file
  fs.createReadStream('dataset.csv')
    .pipe(csv())
    .on('data', (row) => {
      courseNames.push(row['Course']);
      dates.push(row['Date']);
      certificateUrls.push(row['Certificate Url']);
      instructorNames.push(row['Instructor Name']);
      studentNames.push(row['Name']);
      courseLengths.push(row['Course Length']);
    })
    .on('end', async () => {
      // Deploy the contract
      const studentDataset = await StudentDataset.deploy(
        courseNames,
        dates,
        certificateUrls,
        instructorNames,
        studentNames,
        courseLengths
      );

      await studentDataset.deployed();

      console.log('Contract deployed to:', studentDataset.address);

      // Interact with the contract
      const recordCount = await studentDataset.getRecordCount();
      console.log('Number of Records:', recordCount.toString());

      const record = await studentDataset.getStudentRecord(0);
      console.log('First Record:', record);
    });
}

main()
  .then(() => process.exit(0))
  .catch((error) => {
    console.error(error);
    process.exit(1);
  });
