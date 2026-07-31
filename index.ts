#!/usr/bin/env node

interface BrainPrintInput {
  profile: string;
  assessmentType: string;
  brainPrint: number;
  cognitiveProfile: number;
  learningStyle: number;
  personalityInsight: number;
  careerPathway: number;
  leadershipWorkplace: number;
}

interface BrainPrintOutput {
  profile: string;
  assessmentType: string;
  brainPrintScore: number;
  cognitiveProfileScore: number;
  learningStyleScore: number;
  personalityInsightScore: number;
  careerPathwayScore: number;
  leadershipWorkplaceScore: number;
  overallBrainPrintIndex: number;
  priorityAction: string;
  multipleIntelligence: Record<string, number>;
}

function getStatus(score: number): string {
  if (score <= 30) return "Critical";
  if (score <= 60) return "At Risk";
  if (score <= 80) return "Healthy";
  return "Excellent";
}

function getPriorityAction(scores: Record<string, number>): string {
  const labels: Record<string, string> = {
    brainPrint: "BrainPrint",
    cognitiveProfile: "Cognitive Profile",
    learningStyle: "Learning Style",
    personalityInsight: "Personality Insight",
    careerPathway: "Career Pathway",
    leadershipWorkplace: "Leadership & Workplace",
  };
  const lowest = Object.entries(scores).reduce((a, b) => a[1] < b[1] ? a : b);
  return `${labels[lowest[0]]} (${lowest[1]}/100 — act first)`;
}

function getMultipleIntelligence(cognitive: number, learning: number, personality: number): Record<string, number> {
  return {
    "Logical-Mathematical": Math.min(100, Math.round(cognitive * 1.07)),
    "Linguistic": Math.min(100, Math.round(cognitive * 1.0)),
    "Spatial-Visual": Math.min(100, Math.round(learning * 1.0)),
    "Interpersonal": Math.min(100, Math.round(personality * 1.03)),
  };
}

export function analyzeBrainPrint(input: BrainPrintInput): BrainPrintOutput {
  const scores = {
    brainPrint: input.brainPrint,
    cognitiveProfile: input.cognitiveProfile,
    learningStyle: input.learningStyle,
    personalityInsight: input.personalityInsight,
    careerPathway: input.careerPathway,
    leadershipWorkplace: input.leadershipWorkplace,
  };
  const overallBrainPrintIndex = Math.round(
    Object.values(scores).reduce((a, b) => a + b, 0) / 6
  );
  return {
    profile: input.profile,
    assessmentType: input.assessmentType.split("-").map(w => w.charAt(0).toUpperCase() + w.slice(1)).join(" "),
    brainPrintScore: input.brainPrint,
    cognitiveProfileScore: input.cognitiveProfile,
    learningStyleScore: input.learningStyle,
    personalityInsightScore: input.personalityInsight,
    careerPathwayScore: input.careerPathway,
    leadershipWorkplaceScore: input.leadershipWorkplace,
    overallBrainPrintIndex,
    priorityAction: getPriorityAction(scores),
    multipleIntelligence: getMultipleIntelligence(input.cognitiveProfile, input.learningStyle, input.personalityInsight),
  };
}

const args = process.argv.slice(2);
const profile = args[0] || "student-profile";
const assessmentType = args[1] || "student-dmit";
const brainPrint = parseInt(args[2]) || 88;
const cognitiveProfile = parseInt(args[3]) || 82;
const learningStyle = parseInt(args[4]) || 85;
const personalityInsight = parseInt(args[5]) || 78;
const careerPathway = parseInt(args[6]) || 90;
const leadershipWorkplace = parseInt(args[7]) || 80;

const result = analyzeBrainPrint({
  profile, assessmentType, brainPrint, cognitiveProfile,
  learningStyle, personalityInsight, careerPathway, leadershipWorkplace,
});

console.log(`Profile: ${result.profile}`);
console.log(`Assessment Type: ${result.assessmentType}`);
console.log("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━");
console.log(`BrainPrint Score:              ${result.brainPrintScore}/100  [${getStatus(result.brainPrintScore)}]`);
console.log(`Cognitive Profile Score:       ${result.cognitiveProfileScore}/100  [${getStatus(result.cognitiveProfileScore)}]`);
console.log(`Learning Style Score:          ${result.learningStyleScore}/100  [${getStatus(result.learningStyleScore)}]`);
console.log(`Personality Insight Score:     ${result.personalityInsightScore}/100  [${getStatus(result.personalityInsightScore)}]`);
console.log(`Career Pathway Score:          ${result.careerPathwayScore}/100  [${getStatus(result.careerPathwayScore)}]`);
console.log(`Leadership & Workplace Score:  ${result.leadershipWorkplaceScore}/100  [${getStatus(result.leadershipWorkplaceScore)}]`);
console.log("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━");
console.log(`Overall BrainPrint Index:      ${result.overallBrainPrintIndex}/100`);
console.log(`Priority Action:               ${result.priorityAction}`);
console.log("\nMultiple Intelligence Profile:");
Object.entries(result.multipleIntelligence).forEach(([intel, score]) => {
  console.log(`  ${intel.padEnd(26)} ${score}/100`);
});
